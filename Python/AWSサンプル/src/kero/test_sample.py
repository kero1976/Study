import boto3
from moto import mock_s3
import pytest

@pytest.fixture
def s3_client():
    with mock_s3():
        yield boto3.client('s3')

def test_get_object(s3_client):
    bucket_name = 'my-bucket'
    object_key = 'example.txt'

    # バケットとオブジェクトを作成
    s3_client.create_bucket(Bucket=bucket_name)
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body='Hello, World!')

    # オブジェクトの取得
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')

    # アサーション
    assert content == 'Hello, World!'