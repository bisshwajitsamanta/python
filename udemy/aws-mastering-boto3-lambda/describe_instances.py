import boto3

client = boto3.client('ec2')
resp = client.describe_instances(
    Filters = [
        {
            # 'Name': 'instance-state-name',
            # 'Values': ['running']
            'Name': 'tag:Name',
            'Values': ['tagged_instance']
        }
    ]
)

for value in resp.get('Reservations'):
    for instances in value.get("Instances"):
        print(f'The Instances which are created {instances.get("InstanceId")} of type {instances.get("InstanceType")}')

# instances_list =[[instances.get("InstanceId") for instances in value.get("Instances")]for value in resp.get('Reservations')]
# print(instances_list)