import boto3
from logging import getLogger
from botocore.exceptions import ClientError

logger = getLogger(__name__)

class Sample():
    def sample1(data1, data2, data3):
        client = boto3.client("dynamodb")


        response = client.put_item(
            Item={
                'AlbumTitle': {
                    'S': data1,
                },
                'Artist': {
                    'S': data2,
                },
                'SongTitle': {
                    'S': data3,
                },
            },
            ReturnConsumedCapacity='TOTAL',
            TableName='Music',
        )

        print(response)

class ResourceDataPut():
    """
    Resourceを使用してTableにデータを登録する
    """
    def __init__(self, dynamodb):
        logger.debug({
            "action": "init",
            "param":{
                "dynamodb": dynamodb,
            }
        })
        self.dynamodb = dynamodb


    def batch_writer(self, tablename, items):
        """
        データを一括登録
        """
        table = self.dynamodb.Table(tablename)
        try:
            with table.batch_writer() as batch:
                for item in items:
                    response = batch.put_item(Item=item)
                    logger.debug(response)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def put_item(self, tablename, item, condition_expression):
        table = self.dynamodb.Table(tablename)
        try:
            response = table.put_item(
                        Item=item,
                        ConditionExpression=condition_expression
                    )
            logger.debug(response)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                logger.info("既に登録済です")
                return False
            else:
                logger.error({
                "action": "fail",
                "message": "その他のクライアントエラー",
                "exception": e})
        except Exception as e:
            logger.error({
            "action": "fail",
            "message": "その他のエラー",
            "exception": e})
            return False