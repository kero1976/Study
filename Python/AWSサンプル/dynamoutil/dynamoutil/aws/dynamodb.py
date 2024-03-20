import boto3

from logging import getLogger
import logging
logger = getLogger(__name__)

logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("boto3").setLevel(logging.ERROR)

class DynamoDb:
    
    def get_resource(self):
        logger.debug("get_resource start")
        try:
            resource = boto3.resource('dynamodb')
            logger.debug("get_resource success")
            logger.debug(type(resource))
            return resource
        except Exception as e:
            logger.error(f"get_resource fail.({e})")
        
