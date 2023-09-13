import json
from datetime import datetime, timedelta, timezone

import boto3

client = boto3.client('ec2')


def delete_snapshots():
    resp = client.describe_snapshots(
        OwnerIds=['self']
    )
    for snapshot in resp['Snapshots']:
        start_time = snapshot.get('StartTime')
        delete_time = datetime.now(tz=timezone.utc) - timedelta(days=730)
        if delete_time > start_time:
            try:
                snapshot_id = snapshot.get('SnapshotId')
                print(f'{snapshot_id} Snapshot ID is getting deleted!')
                client.delete_snapshot(SnapshotId=snapshot_id)
                return f'{snapshot_id} Snapshot ID is getting deleted!'

            except Exception as ex:
                print(f'Exception occurred:{ex}')
                print("Skipping this snapshot")
                continue


def lambda_handler(event, context):
    snapshot_ids = delete_snapshots()
    return {
        'StatusCode': 200,
        'body': json.dumps(snapshot_ids)
    }
