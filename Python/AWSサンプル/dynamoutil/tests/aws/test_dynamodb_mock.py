import pytest
import boto3
from moto import mock_aws
from dynamoutil.aws.dynamodb import dynamodb_all_data, DynamoDb
from dynamoutil.localfile.app import create_dir_file
from dynamoutil.localfile.file_reader import FileReader
from boto3.dynamodb.types import Decimal
import json
import decimal

DYNAMO_REGION = 'ap-northeast-1'
DYNAMO_TABLE_NAME = 'auth_table'



def create_table(resource):
    table = resource.create_table(
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
    return table


@mock_aws()
def test_mock_get_all():
    ddb = boto3.resource('dynamodb')
    
    table = create_table(ddb)

    # Dummyデータ投入
    table.put_item(
            Item={
                'id': '0001',
                'name': 'satoh',
                'company': 'A',
                'num': Decimal('1.5'),
                "foo":{
                    "bar1": "a",
                    "bar2": "b"
                },
                "lists": ["A", "B"]
            },
    )


    alldata = dynamodb_all_data(DYNAMO_TABLE_NAME)
    print(alldata)
    create_dir_file(DYNAMO_TABLE_NAME, alldata)
    
@pytest.mark.shijo
@mock_aws()
def test_mock_insert():
    ddb = boto3.resource('dynamodb')
    table = create_table(ddb)
    db = DynamoDb()
    file = FileReader("./20240331/20240331_100813_auth_table.json")
    datas = file.read()
    data2 = json.loads(datas, parse_float=decimal.Decimal)
    db.put_datas(table, data2)
    alldata = dynamodb_all_data(DYNAMO_TABLE_NAME)
    print(alldata)
