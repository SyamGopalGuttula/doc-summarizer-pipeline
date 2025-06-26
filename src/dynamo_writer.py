import boto3
from botocore.exceptions import ClientError

def write_to_dynamodb(table_name, document_name, summary, region="us-east-1"):
    """
    Writes summary data to a DynamoDB table.
    """
    dynamodb = boto3.resource("dynamodb", region_name=region)
    table = dynamodb.Table(table_name)

    try:
        response = table.put_item(
            Item={
                "DocumentName": document_name,
                "Summary": summary
            }
        )
        return response
    except ClientError as e:
        raise RuntimeError(f"Failed to write to DynamoDB: {e}")
