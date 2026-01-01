import boto3

ec2=boto3.client('ec2')

snapshots=ec2.describe_snapshots(OwnerIds=['self'])

for snapshot in snapshots['Snapshots']:     
    volumeId=snapshot['VolumeId']
    snapshotId=snapshot['SnapshotId']

    if not volumeId:
        ec2.delete_snapshot(SnapshotId=snapshotId)
        print(f"Deleted snapshot {snapshotId} with no associated volume.")
    else:
        try:
            volume_details=ec2.describe_volumes(VolumeIds=[volumeId])
            if not volume_details['Volumes'][0]['Attachments']:
                ec2.delete_snapshot(SnapshotId=snapshotId)
                print(f"Deleted snapshot {snapshotId} associated with detached volume {volumeId}.")
        except ec2.exceptions.ClientError as e:
            if 'InvalidVolume.NotFound' in str(e):
                ec2.delete_snapshot(SnapshotId=snapshotId)
                print(f"Deleted snapshot {snapshotId} associated with non-existent volume {volumeId}.")
            else:
                print(f"Error checking volume {volumeId} for snapshot {snapshotId}: {e}")