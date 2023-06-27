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



def getStringData(s3, bucket_name, key):
    logger.info({"action": 'start',
                'param': {
                    's3': s3,
                    'bucket_name': bucket_name,
                    'key': key
                }})

    if not bucket_name or not key:
        msg = {
            "action": "fail",
            "msg": "Parameter is None.",
        }
        logger.debug(msg)
        logger.error("Bucket name or key not specified.")
        return
    # バケット内のオブジェクトのリストを取得
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        data = response["Body"].read().decode("utf-8")
        
        logger.info({
            'action': 'success',
            'return': data,
            "cnt": len(data)
        })
        return data
    except botocore.exceptions.ClientError as err:
        msg = {
            "action": "fail",
            "msg": "get_object err",
            "exception": err,
            "type": type(err),
            "traceback": traceback.format_exception(err)
        }
        code = err.response["Error"]["Code"]
        logger.error(f"S3 Request Error.({code}):Bucketname={bucket_name}")
        logger.debug(msg)
        return
    except botocore.exceptions.NoCredentialsError as err:
        msg = {
            "action": "fail",
            "msg": "get_object err",
            "exception": err,
            "type": type(err)
        }
        logger.error(f"NoCredentialsError.")
        logger.debug(msg)
        return
    except Exception as err:
        msg = {
            "action": "fail",
            "msg": "get_object err",
            "exception": err,
            "type": type(err),
            "traceback": traceback.format_exception(err)
        }
        logger.debug(msg)
        return



def s3listInput():
    logger.debug({"action": 'start'})
    buketname = input(colored("[+]Bucket Name:", "green"))
    key = input(colored("[+]Key Name:", "green"))
    getStringData(boto3.client("s3"), buketname, key)

if __name__ == '__main__':
    s3listInput()