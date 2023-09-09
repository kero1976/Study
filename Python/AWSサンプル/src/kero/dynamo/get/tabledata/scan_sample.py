import boto3
from logging import getLogger
from botocore.exceptions import EndpointConnectionError, NoCredentialsError


logger = getLogger(__name__)

class MyAppAWSException(Exception):
    def __init__(self, message, e):
        self.__message = message
        self.__e = e

    @property
    def message(self):
        return self.__message
    



class SampleDynamo():
    def __init__(self, client, table="Music") -> None:
        """_summary_

        Args:
            client (client): _description_
            table (str, optional): _description_. Defaults to "Music".
        """
        self.client = client
        self.table = table
        logger.debug({
            "action": "init",
            "param":{
                "client": client,
                "table": table
            }
        })
    

    def scan(self, hash: str):
        response = self.scan_getresponse(hash)
        for i in response:
            print(i + "\n")
        return response

    def scan_getresponse(self, hash: str) -> dict:
        """スキャンを実行し、レスポンスを取得する

        Args:
            hash (str): _description_

        Raises:
            MyAppAWSException: _description_

        Returns:
            _type_: _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "hash": hash
            }
        })
        try:
            response = self.client.scan(
                ExpressionAttributeNames={
                    '#AT': 'AlbumTitle',
                    '#ST': 'SongTitle',
                },
                ExpressionAttributeValues={
                    ':a': {
                        'S': hash,
                    },
                },
                FilterExpression='Artist = :a',
                ProjectionExpression='#ST, #AT',
                TableName='Music',
            )
        except (EndpointConnectionError, NoCredentialsError) as e:
            logger.error(
                {
                "action": "fail",
                "param": {
                    "hash": hash
                },
                "exception": e
            })
            raise MyAppAWSException("AWSとのコネクションエラー。", e)
        
        logger.debug(
            {
            "action": "success",
            "param": {
                "hash": hash
            },
            "return": response
        })
        return response