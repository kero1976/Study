import pytest
from moto import mock_dynamodb
from kero.dynamo.dynamotable import dynamo2
import boto3


@pytest.fixture(autouse=True)
def setup_ddb():
    mock = mock_dynamodb()
    mock.start()
    prepare_foo_table()
    yield
    mock.stop()


def test1():
    dynamodb = boto3.resource("dynamodb")
    dynamo = dynamo2(dynamodb)
    response = dynamo.list_all_tables()
    assert response == []


def prepare_foo_table():
    table_name = "foo"
    dynamodb = boto3.resource("dynamodb")

    # テーブルの作成
    foo_table_def = {
        "AttributeDefinitions": [{"AttributeName": "dataId", "AttributeType": "S"}],
        "KeySchema": [{"AttributeName": "dataId", "KeyType": "HASH"}],
        "BillingMode": "PAY_PER_REQUEST",
    }
    dynamodb.create_table(
        TableName=table_name,
        **foo_table_def,
    )

    # テーブルにデータを投入
    data_items = [
        {"PutRequest": {"Item": {"dataId": "1", "data": "data_01"}}},
        {"PutRequest": {"Item": {"dataId": "2", "data": "data_02"}}},
    ]
    table = dynamodb.Table(table_name)
    for item in data_items:
        table.put_item(Item=item["PutRequest"]["Item"])
