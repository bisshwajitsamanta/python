import boto3

rds_client = boto3.client('rds')


def helper(db):
    get_tags = db['TagList']
    for tags in get_tags:
        if tags['Key'] == 'stop' and tags['Value'] == 'yes':
            print(f"Database {db['DBInstanceIdentifier']} Status is :: {db['DBInstanceStatus']}")


def describe_rds():
    dbs = rds_client.describe_db_instances()
    for db in dbs['DBInstances']:
        try:
            if db['DBInstanceStatus'] == 'stopped':
                helper(db)
            if db['DBInstanceStatus'] == 'available':
                helper(db)
                response = rds_client.stop_db_cluster(DBClusterIdentifier=db['DBClusterIdentifier'])
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print(f"Stopping Instance: {db['DBInstanceIdentifier']}")
        except Exception as e:
            print(f"Cannot Stop the DB Instance:{db['DBInstanceIdentifier']} with exception: {e}")
            print("Exception:", e)


describe_rds()
