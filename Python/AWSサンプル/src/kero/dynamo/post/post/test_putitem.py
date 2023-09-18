from kero.dynamo.post.data.putitem import ResourceDataPut
import boto3
import logging
import pytest

import botocore
from botocore.session import Session
from botocore.config import Config


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
    def test_data30(self, logcontrol):

        dynamo = boto3.resource("dynamodb", endpoint_url='http://localhost:8000')
        putitem = ResourceDataPut(dynamo)
        items = [
                {"id": "b01"},
                {"id": "b02"},
                {"id": "b03"},
                {"id": "b04"},
                {"id": "b05"},
                {"id": "b06"},
                {"id": "b07"},
                {"id": "b08"},
                {"id": "b09"},
                {"id": "b10"},
                {"id": "b11"},
                {"id": "b12"},
                {"id": "b13"},
                {"id": "b14"},
                {"id": "b15"},
                {"id": "b16"},
                {"id": "b17"},
                {"id": "b18"},
                {"id": "b19"},
                {"id": "b20"},
                {"id": "b21"},
                {"id": "b22"},
                {"id": "b23"},
                {"id": "b24"},
                {"id": "b25"},
                {"id": "b26"},
                {"id": "b27"},
                {"id": "b28"},
                {"id": "b29"},
                {"id": "b30"},
        ]
        assert putitem.batch_writer('sample', items) == None

    @pytest.mark.skip
    def test_put_item_ng(self, logcontrol):

        dynamo = boto3.resource("dynamodb", endpoint_url='http://localhost:8000')
        putitem = ResourceDataPut(dynamo)
        items =  {"id": "a1"}
        
        assert putitem.put_item('sample', items, "attribute_not_exists(id)") == False

    def test_put_item_ng_network(self, logcontrol):
 
        dynamo = boto3.resource("dynamodb", endpoint_url='http://localhost:8001', config=Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 1}))
        putitem = ResourceDataPut(dynamo)
        items =  {"id": "a4"}
        
        assert putitem.put_item('sample', items, "attribute_not_exists(id)") == False

    @pytest.mark.skip
    def test_put_item(self, logcontrol):

        dynamo = boto3.resource("dynamodb", endpoint_url='http://localhost:8000')
        putitem = ResourceDataPut(dynamo)
        items =  {"id": "a3"}
        
        assert putitem.put_item('sample', items, "attribute_not_exists(id)") == True