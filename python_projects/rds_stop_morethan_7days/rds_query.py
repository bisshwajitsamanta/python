# import boto3
#
# rds_client = boto3.client('rds')
#
#
# def describe_rds(key, value):
#     response = rds_client.describe_db_instances(
#         Filters=[{
#             'Name': 'tag:' + key,
#             'Values': [value]
#         }]
#     )
#     for db in response['DBInstances']:
#         print(f"DB Instance Details: {db['DBInstanceIdentifier']}")
#
#
# tag_key = 'Instance_State'
# tag_value = 'Stop_Permanently'
#
# describe_rds(tag_key,tag_value)

