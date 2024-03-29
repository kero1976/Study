from kero.dynamo.get.tabledata.query_sample import SampleDynamo2
import boto3
import logging
import pytest
from kero.dynamo.get.tabledata.query_sample import MyAppAWSException
import botocore

class TestSample():

    @pytest.fixture(scope='class')
    def logcontrol(self):
        """不要なログを出さないように
        """
        botocore = logging.getLogger("botocore")
        botocore.setLevel(logging.ERROR)
        urllib3 = logging.getLogger("urllib3")
        urllib3.setLevel(logging.ERROR)
        yield
        print("後処理")

    @pytest.mark.skip
    def test1(self, logcontrol):

        client = boto3.client("dynamodb")
        dynamo = SampleDynamo2(client)
        assert dynamo.query('No One You Know') == None

    @pytest.mark.skip("ネットワークを無効にして、クレデンシャルファイルを有効にする必要がある")
    def test_connect_error(self, logcontrol):
        client = boto3.client("dynamodb")
        dynamo = SampleDynamo2(client)
        with pytest.raises(MyAppAWSException) as e:
            dynamo.query('No One You Know') 
            
        # エラーメッセージを検証
        assert e.value.args[0] == "AWSとのコネクションエラー。"
        assert type(e.value.args[1]) == botocore.exceptions.EndpointConnectionError

    @pytest.mark.skip("クレデンシャルファイルをリネームする必要がある")
    def test_authencate_error(self, logcontrol):

        try:
            client = boto3.client("dynamodb")
            print("OK")
        except Exception as e:
            print("NG")
            print(e)

        dynamo = SampleDynamo2(client)
        with pytest.raises(MyAppAWSException) as e:
            dynamo.query('No One You Know') 
            
        # エラーメッセージを検証
        assert e.value.args[0] == "AWSとのコネクションエラー。"
        assert type(e.value.args[1]) == botocore.exceptions.NoCredentialsError

    @pytest.mark.skip
    def test_ok(self, logcontrol):

        client = boto3.client("dynamodb")
        dynamo = SampleDynamo2(client)
        assert len(dynamo.query('No One You Know')) == 2

    # @pytest.mark.skip
    def test_no_table(self, logcontrol):

        client = boto3.client("dynamodb")
        dynamo = SampleDynamo2(client, "hoge")
        with pytest.raises(MyAppAWSException) as e:
            dynamo.query('No One You Know') 
            
        # エラーメッセージを検証
        assert e.value.args[0] == "Table(hoge)が存在しませんでした。"
        assert type(e.value.args[1]) == client.exceptions.ResourceNotFoundException

    @pytest.mark.skip
    def test_no_data(self, logcontrol):

        client = boto3.client("dynamodb")
        dynamo = SampleDynamo2(client)
        assert len(dynamo.query('hoge')) == 0
