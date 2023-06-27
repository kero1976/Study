"""
S3にファイルがあるかどうかを確認する
"""
import os
import traceback
from logging import config, getLogger

import boto3
import botocore
from termcolor import colored, cprint

config.fileConfig(os.path.join(os.path.dirname(__file__) , "../../logging.ini"), encoding='utf-8')
logger = getLogger(__name__)

def s3list_filter(bucket_name, prefix):
    logger.info({"action": 'start',
                'param': {
                    'bucket_name': bucket_name,
                    "prefix": prefix
                }})
    list = []
    if not bucket_name:
        msg = {
            "action": "fail",
            "msg": "Parameter is None.",
        }
        logger.debug(msg)
        logger.error("Bucket name not specified.")
        return
    # バケット内のオブジェクトのリストを取得
    try:
        s3_resource = boto3.resource('s3')
        a = s3_resource.Bucket(bucket_name).objects.filter(Prefix=prefix)
        list = [k.key for k in a]

        logger.info({
            'action': 'success',
            'return': list,
            "cnt": len(list)
        })
        return list
    except botocore.exceptions.ClientError as err:
        msg = {
            "action": "fail",
            "msg": "list_objects_v2 err",
            "exception": err,
            "type": type(err),
            "traceback": traceback.format_exception(err)
        }
        code = err.response["Error"]["Code"]
        logger.error(f"S3 Request Error.({code}):Bucketname={bucket_name}")
        logger.debug(msg)
        return
    except Exception as err:
        msg = {
            "action": "fail",
            "msg": "list_objects_v2 err",
            "exception": err,
            "type": type(err),
            "traceback": traceback.format_exception(err)
        }
        logger.debug(msg)
        return

def s3listInput():
    logger.debug({"action": 'start'})
    buketname = input(colored("[+]Bucket Name:", "green"))
    prefix = input(colored("[+]prefix:", "green"))
    s3list_filter(buketname, prefix)

if __name__ == '__main__':
    s3listInput()