import boto3

from logging import getLogger
import logging
logger = getLogger(__name__)

logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("boto3").setLevel(logging.ERROR)

class DynamoDb:
    
    def get_resource(self, profile=None, region="ap-northeast-1"):
        """リソースの取得

        Returns:
            _type_: _description_
        """

        logger.debug(f"get_resource start(profile={profile}, region={region})")
        try:
            my_session = boto3.Session(profile_name=profile, region_name=region)
            resource = my_session.resource('dynamodb')
            logger.debug("get_resource success")
            return resource
        except Exception as e:
            logger.error(f"get_resource fail.({e})")
            raise
        

    def get_table(self, dynamodb, table_name):
        logger.debug(f"get_table start(dynamodb={dynamodb}, table_name={table_name})")
        table = dynamodb.Table(table_name)
        logger.debug("get_table success")
        return table


    def get_all_data(self, table):
        logger.debug(f"get_all_data start(table={table})")
        try:
            response = table.scan()
            items = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items.extend(response['Items'])
            
            logger.debug("get_all_data success")
            return items
        except Exception as e:
            logger.error(f"get_all_data fail.({e})")