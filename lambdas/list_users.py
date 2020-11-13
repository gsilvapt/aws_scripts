import json, boto3

def lambda_hanlder(event, context):
    """
    This function, when executed, will list all IAM users.
    This is in the context of IAM resources and authorization.
    """
    client = boto3.client('iam')
    response = client.list_users()

    print("Full output returned by the API:")
    print(response)

    print("Alternatively, a formatted response:")
    for item in response["Users"]:
        print(f"{item['UserName']} has the arn {item{'Arn']}")

    return True

