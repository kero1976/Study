
import boto3
from boto3.dynamodb.conditions import Key, Attr

def sample1():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("sample")
    response = table.query(
        KeyConditionExpression=Key('id1').eq("1")
    )
    print(response)

def sample2(client):
    # client = boto3.client("dynamodb")
    response = client.query(
        ExpressionAttributeValues={
            ':v1': {
                'S': 'foo',
            },
        },
        KeyConditionExpression='NewValue = :v1',
        ProjectionExpression='id1',
        TableName='sample',
    )

    print(response["Items"])


client = boto3.client("dynamodb")
sample2(client)