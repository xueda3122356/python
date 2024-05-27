# import all the modules and libraries
import boto3
import boto3.session

# open management console
aws_management_console = boto3.session.Session(profile_name='default')

# open ec2 console
ec2_console = aws_management_console.client('ec2')

# use boto3 documentation to get more information
result = ec2_console.describe_instances()['Reservations']

for each_instance in result:
    for value in each_instance['Instances']:
        print(value['InstanceId'])