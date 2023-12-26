"""AWS Lambda resource tagger for new Amazon EC2 instances & attached EBS volumes.
   Amazon EventBridge triggers this AWS Lambda function when AWS CloudTrail detects
   a RunInstances API event with VPC-ID.
   This Lambda function extracts relevant information
   from that API event to retrieve resource tags assigned to the VPC-ID,
   & SSM parameters.  Next, this Lambda applies the retrieved tags to the newly created
   Amazon EC2 instances & their attached EBS volumes listed in the CloudTrail event.
"""

import json
import logging

import boto3
import botocore

logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger(__name__)

# Instantiate Boto3 clients & resources for every AWS service API called
ec2_client = boto3.client("ec2")
ec2_resource = boto3.resource("ec2")
sns_client = boto3.client("sns")


def send_email(instance_id):
    sts_cli = get_client('sts', profile, region)
    acc_id = sts_cli.get_caller_identity().get('Account')
    runtime_region = os.environ['AWS_REGION']
    mess = "Following instance has been tagged:\n"
    mess += "    Instance Id:- {}\n\n".format(instance_id)
    mess += "Regards,\nProdOps Team"
    response = sns_cli.publish(
        TopicArn="arn:aws:sns:{}:{}:{}".format(runtime_region, acc_id, os.environ["Sns_Topic"]),
        Message=mess
    )
    return response


def get_vpc_tags(vpc_id: str) -> list:
    tag_list = []
    """ Get VPC Tag details

    Args:
        vpc_id: VPC ID of the Resource

    Returns:
        tag_list: It contains a list of dictionary of Tags

    """
    response = ec2_client.describe_vpcs(
        VpcIds=[vpc_id]
    )

    for i in response['Vpcs']:
        response_tag_list = i.get("Tags")
        for index in range(len(response_tag_list)):
            tag_list.append(response_tag_list[index])

    for d in tag_list:
        if d["Key"] == "Name":
            tag_list.remove(d)
            break

    return tag_list


def set_ec2_instance_attached_vols_tags(ec2_instance_id, resource_tags):
    """Applies a list of passed resource tags to the Amazon EC2 instance.
       Also applies the same resource tags to EBS volumes attached to instance.

    Args:
        ec2_instance_id: EC2 instance identifier
        resource_tags: a list of key:string,value:string resource tag dictionaries

    Returns:
        Returns True if tag application successful and False if not

    Raises:
        AWS Python API "Boto3" returned client errors
    """
    global eni_id
    try:
        response = ec2_client.create_tags(
            Resources=[ec2_instance_id], Tags=resource_tags
        )
        response = ec2_client.describe_volumes(
            Filters=[{"Name": "attachment.instance-id", "Values": [ec2_instance_id]}]
        )
        network_response = ec2_client.describe_network_interfaces(
            Filters=[{"Name": "attachment.instance-id", "Values": [ec2_instance_id]}]
        )

        for network in network_response.get("NetworkInterfaces"):
            eni_id = network['NetworkInterfaceId']

        eni_tag = ec2_client.create_tags(
            Resources=[eni_id], Tags=resource_tags
        )

        try:
            for volume in response.get("Volumes"):
                ec2_vol = ec2_resource.Volume(volume["VolumeId"])
                vol_tags = ec2_vol.create_tags(Tags=resource_tags)
            return True

        except botocore.exceptions.ClientError as error:
            log.error(f"Boto3 API returned error: {error}")
            log.error(f"No Tags Applied To: {volume['VolumeId']}")
            return False

    except botocore.exceptions.ClientError as error:
        log.error(f"Boto3 API returned error: {error}")
        log.error(f"No Tags Applied To: {ec2_instance_id}")
        return False


def cloudtrail_event_parser(event):
    """Extract list of new EC2 instance attributes, creation date, ,
    SSO User ID from the AWS CloudTrail resource creation event.

    Args:
        event: a cloudtrail event in python dictionary format

    Returns a dictionary containing these keys and their values:
        instances_set: list of EC2 instances & parameter dictionaries
        resource_date: date the EC2 instance was created

    Raises:
        none
    """
    returned_event_fields = {}

    # check if the resource created under the VPC ID & get that VPC ID
    itemsArray = event.get("detail").get("responseElements").get("instancesSet").get("items")
    for i in itemsArray:
        returned_event_fields["vpc_id"] = i.get("vpcId")

    # Extract & return the list of new EC2 instance(s) and their parameters
    returned_event_fields["instances_set"] = (
        event.get("detail").get("responseElements").get("instancesSet")
    )

    # Extract the date & time of the EC2 instance creation
    returned_event_fields["resource_date"] = event.get("detail").get("eventTime")

    return returned_event_fields


def lambda_handler(event, context):
    """

    Args:
        event: Event is the Dictionary which we are getting from Cloudwatch Logs
        context:

    Returns:

    """
    resource_tags = []

    # Parse the passed CloudTrail event and extract pertinent EC2 launch fields
    event_fields = cloudtrail_event_parser(event)

    if event_fields.get("vpc_id"):
        parameter_resource_tags = get_vpc_tags(
            vpc_id=event_fields["vpc_id"]
        )
        if parameter_resource_tags:
            resource_tags += parameter_resource_tags

    # Check for event date & time in returned CloudTrail event field
    # and append as resource tag
    if event_fields.get("resource_date"):
        resource_tags.append(
            {"Key": "Date created", "Value": event_fields["resource_date"]}
        )

    # Tag EC2 instances listed in the CloudTrail event
    if event_fields.get("instances_set"):
        for item in event_fields.get("instances_set").get("items"):
            ec2_instance_id = item.get("instanceId")
            if set_ec2_instance_attached_vols_tags(ec2_instance_id, resource_tags):
                log.info("'statusCode': 200")
                log.info(f"'Resource ID': {ec2_instance_id}")
                log.info(f"'body': {json.dumps(resource_tags)}")
                send_email(ec2_instance_id)
            else:
                log.info("'statusCode': 500")
                log.info(f"'No tags applied to Resource ID': {ec2_instance_id}")
                log.info(f"'Lambda function name': {context.function_name}")
                log.info(f"'Lambda function version': {context.function_version}")
    else:
        log.info("'statusCode': 200")
        log.info(f"'No Amazon EC2 resources to tag': 'Event ID: {event.get('id')}'")
