"""
Create a list of aws services using Python
"""
# creating an empty list
list_of_aws_services = []

# populating the list-of-aws-services using append
list_of_aws_services.append("S3")
list_of_aws_services.append("Lambda")
list_of_aws_services.append("EC2")
list_of_aws_services.append("DynamoDB")
list_of_aws_services.append("SNS")
list_of_aws_services.append("SQS")
list_of_aws_services.append("CloudFormation")
list_of_aws_services.append("Security group")

# Printing the list and the length of the list.
print(list_of_aws_services)
print(len(list_of_aws_services))

# Remove two specific services from the list by name or by index
list_of_aws_services.remove("Lambda")
list_of_aws_services.remove("CloudFormation")

# Print the new list and the new length of the list.
print(list_of_aws_services)
print(len(list_of_aws_services))

