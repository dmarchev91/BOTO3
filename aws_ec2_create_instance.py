#Lets create ec2-instance via BOTO3
import boto3
def create_ec2_instance():
   try:
        print("Creating EC2-Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-02b4e72b17337d6c1",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="DamyanKey"
        )
   except Exception as e:
       print(e)

create_ec2_instance()
