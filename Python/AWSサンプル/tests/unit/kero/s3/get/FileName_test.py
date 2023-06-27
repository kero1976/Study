from kero.s3.get.FileName import s3list
import boto3
import pytest
from moto import mock_s3

@pytest.mark.skip("一時的に無効化")
def test_s3list():
    print('START:')
    list = s3list(boto3.client("s3"), 'u10.jp')
    assert list == ['DebugPass.zip', 'abc', 'index.html', 'log4j.xml', 'sample/', 'sample/test1.txt', 'sample/test2.txt', 'sample/test3.txt']

@pytest.fixture
def s3_client():
    with  mock_s3():
        yield boto3.client('s3', region_name='us-east-1')




def test_mock(s3_client):
    s3_client.create_bucket(Bucket='u10.jp')
    s3_client.put_object(Bucket='u10.jp', Key='hoge', Body='data')
    s3_client.put_object(Bucket='u10.jp', Key='hoge2', Body='data2')
    s3_client.put_object(Bucket='u10.jp', Key='test/foo', Body='data3')
    list = s3list(s3_client., 'u10.jp')
    assert list == ['hoge', 'hoge2', 'test/foo']