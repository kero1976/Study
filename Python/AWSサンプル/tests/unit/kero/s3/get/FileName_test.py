from kero.s3.get.FileName import s3list
import boto3
import pytest
from moto import mock_s3


def test_s3list():
    print('START:')
    list = s3list(boto3.client("s3"), 'u10.jp')
    assert list == ['DebugPass.zip', 'abc', 'index.html', 'log4j.xml', 'sample/', 'sample/test1.txt', 'sample/test2.txt', 'sample/test3.txt']