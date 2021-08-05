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


def describe_ec2_instance():
    try:
        print("Describing EC2-Instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances())
    except Exception as e:
        print(e)

def terminate_ec2_instance():
    try:
        print("Terminating EC2-Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

#describe_ec2_instance()
#create_ec2_instance()
terminate_ec2_instance()