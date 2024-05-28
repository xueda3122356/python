# import all the modules and libraries
import boto3
import boto3.session

# open management console
aws_management_console = boto3.session.Session(profile_name="default")

# open ec2 console
ec2_console = aws_management_console.client(service_name='ec2')

# use boto3 documentation to get more information

# stop ec2 instance test-1 
'''ec2_console.stop_instances(
    InstanceIds=['i-04b920c6db7e5c131']
) '''

# start ec2 instance test-1
'''ec2_console.start_instances(
    InstanceIds=['i-04b920c6db7e5c131']
)'''

# terminate ec2 instance test-1
ec2_console.terminate_instances(
    InstanceIds=['i-04b920c6db7e5c131']
)