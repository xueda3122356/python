#import all the modules and libraries 
import boto3
import boto3.session

# Open aws management console
aws_management_console = boto3.session.Session(profile_name='default')

# open iam console
iam_console = aws_management_console.client('iam')

# use boto3 documentation to get more information
result = iam_console.list_users()

print(result)

for each_user in result['Users']:
    print("User name: " + each_user['UserName'])