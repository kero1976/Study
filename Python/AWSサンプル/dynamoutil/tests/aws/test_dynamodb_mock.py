import pytest
import boto3
from moto import mock_aws
from dynamoutil.aws.dynamodb import dynamodb_all_data

DYNAMO_REGION = 'ap-northeast-1'
DYNAMO_TABLE_NAME = 'auth_table'



@mock_aws()
def test_mock_get_all():
    ddb = boto3.resource('dynamodb', region_name=DYNAMO_REGION)
    # Dummyテーブルを作る
    table = ddb.create_table(
        TableName=DYNAMO_TABLE_NAME ,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'name',
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # ちょっと待ち時間を置く
    table.wait_until_exists()

    # Dummyデータ投入
    table.put_item(
            Item={
                'id': '0001',
                'name': 'satoh',
                'company': 'A',
            },
    )


    alldata = dynamodb_all_data(DYNAMO_TABLE_NAME)
    print(alldata)