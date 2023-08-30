import boto3

client = boto3.client('ec2')
resp = client.run_instances(ImageId ="ami-051f7e7f6c2f40dc1",
                     InstanceType = "t2.micro",
                     MinCount = 1,
                     MaxCount =1

                     )
for instance in resp.get('Instances'):
    print(instance['InstanceID'])