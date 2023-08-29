import pytest
from kero.s3.get.bucket.get_bucket import GetBucket
from unittest.mock import MagicMock


def test_get_all_bucket_name_mock_ok():
    mock = MagicMock()
    mock.list_buckets.return_value = {"Buckets": [{"Name": "A"}]}
    
    assert GetBucket(mock)._get_all_bucket_name() == ["A"]
