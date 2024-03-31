import boto3

from logging import getLogger
import logging
logger = getLogger(__name__)

logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("boto3").setLevel(logging.ERROR)

def dynamodb_all_data(table_name: str, profile=None):
    db = DynamoDb()
    if profile:
        dynamodb = db.get_resource(profile)
    else:
        dynamodb = db.get_resource()
    table = db.get_table(dynamodb, table_name)
    return db.get_all_data(table)

class DynamoDb:
    """DynamoDBのテスト効率化のためのユーティリティクラス。
    """
    
    def get_resource(self, profile=None, region="ap-northeast-1"):
        """リソースの取得
        プロファイルの指定可能。
        Returns:
            _type_: _description_
        """

        logger.debug(f"get_resource start(profile={profile}, region={region})")
        try:
            if profile:
                my_session = boto3.Session(profile_name=profile, region_name=region)
            else:
                my_session = boto3.Session()
            resource = my_session.resource('dynamodb')
            logger.debug("get_resource success")
            return resource
        except Exception as e:
            logger.error(f"get_resource fail.({e})")
            raise
        

    def get_table(self, dynamodb, table_name: str):
        """Table Resourceの取得

        Args:
            dynamodb (_type_): Service Resource
            table_name (str): TTable name

        Returns:
            _type_: Table Resource
        """
        logger.debug(f"get_table start(dynamodb={dynamodb}, table_name={table_name})")
        table = dynamodb.Table(table_name)
        logger.debug("get_table success")
        return table


    def get_all_data(self, table) -> list[dict]:
        """全件データ取得

        Args:
            table (_type_): dynamodb table resource

        Returns:
            list[dict]: _description_
        """
        logger.debug(f"get_all_data start(table={table})")
        try:
            response = table.scan()
            items = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items.extend(response['Items'])
            
            logger.debug(f"get_all_data success(size={len(items)})")
            return items
        except Exception as e:
            logger.error(f"get_all_data fail.({e})")

    def put_datas(self, table, datas: list[dict]):
        for data in datas:
            table.put_item(
                    Item=data
            )