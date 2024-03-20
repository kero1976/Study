from dynamoutil.aws.dynamodb import DynamoDb
import boto3
from unittest.mock import MagicMock, patch
import pytest

# @pytest.fixture
# def mock_boto3_session(monkeypatch):
#     # boto3.Session()が呼ばれたときにモックを返す
#     mock_session = MagicMock()
#     monkeypatch.setattr("boto3.Session", lambda: mock_session)
#     return mock_session

# def test_get_resource(mock_boto3_session):
#     db = DynamoDb()

    
#     mock_resource = MagicMock()
#     mock_boto3_session.resource.return_value = mock_resource

#     # AWSリソースの取得を実行
#     resource = db.get_resource()

#     # boto3.Session().resource()が正しく呼び出されたかを確認
#     mock_boto3_session.resource.assert_called_once_with("dynamodb")

#     # 返されたAWSリソースが正しいかを確認
#     assert resource == mock_resource
    
    
def test_get_resource2():


    # boto3.Session().resource()をモック化
    with patch("boto3.Session") as mock_session:
        db = DynamoDb()
        mock_resource = MagicMock()
        mock_session.return_value.resource.return_value = mock_resource

        # AWSリソースの取得を実行
        resource =db.get_resource()
        print(resource)
        # boto3.Session().resource()が正しく呼び出されたかを確認
        mock_session.return_value.resource.assert_called_once_with("dynamodb")

        # 返されたAWSリソースが正しいかを確認
        assert resource == mock_resource