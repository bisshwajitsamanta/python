from datetime import datetime, timedelta, timezone
import json
import boto3

client = boto3.client('ec2')


def delete_snapshots():
    resp = client.describe_snapshots(
        OwnerIds=['self']
    )
    deletion_list = [snap.get('SnapshotId') for snap in resp['Snapshots'] if
                     datetime.now(tz=timezone.utc) - timedelta(minutes=5) > snap.get('StartTime')]
    print(f'Deletion SnapshotIds List: {deletion_list}')
    print(f'Deletion SnapshotIds List: {len(deletion_list)}')
    return deletion_list


def lambda_handler(event, context):
    snapshot_ids = delete_snapshots()
    for i in range(len(snapshot_ids)):
        print(f"Hello You {snapshot_ids[i]} are going to be deleted")
        client.delete_snapshot(SnapshotId=snapshot_ids[i])
    return {
        'StatusCode': 200,
        'body': json.dumps(snapshot_ids, default=str)
    }