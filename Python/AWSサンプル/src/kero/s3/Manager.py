from kero.s3.get.bucket.get_bucket import GetBucket
import boto3
from logging import getLogger, StreamHandler, DEBUG, config
import os

logger = getLogger(__name__)
config.fileConfig(os.path.join(os.path.dirname(__file__) , "../logging.ini"), encoding='utf-8')

print(__name__)


client = boto3.client('s3')
bucket = GetBucket(client)


names = bucket._get_all_bucket_name()
print(names)