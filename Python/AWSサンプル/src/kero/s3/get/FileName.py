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



def s3list(s3, bucket_name, prefix=""):
    logger.info({"action": 'start',
                'param': {
                    's3': s3,
                    'bucket_name': bucket_name,
                    'prefix': prefix
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
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
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
    except botocore.exceptions.NoCredentialsError as err:
        msg = {
            "action": "fail",
            "msg": "list_objects_v2 err",
            "exception": err,
            "type": type(err)
        }
        logger.error(f"NoCredentialsError.")
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

    # オブジェクトのリストを表示
    if "Contents" in response:
        for obj in response["Contents"]:
            list.append(obj["Key"])
    else:
        print("バケット内にオブジェクトはありません。")
    logger.info({
        'action': 'success',
        'return': list,
        "cnt": len(list)
    })
    return list


def s3listInput():
    logger.debug({"action": 'start'})
    buketname = input(colored("[+]Bucket Name:", "green"))
    s3list(boto3.client("s3"), buketname)

if __name__ == '__main__':
    s3listInput()