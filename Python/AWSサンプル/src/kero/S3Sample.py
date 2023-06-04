"""
S3にファイルがあるかどうかを確認する
"""
from logging import getLogger, DEBUG, INFO
import boto3
logger = getLogger(__name__)
logger.setLevel(INFO)

logger.info("load...")


def s3list(s3, bucket_name):
    logger.info({"action": 'start',
                  'param':{
                      's3': s3,
                      'bucket_name': bucket_name
                  }})
    list = []

    # バケット内のオブジェクトのリストを取得
    response = s3.list_objects_v2(Bucket=bucket_name)

    # オブジェクトのリストを表示
    if "Contents" in response:
        for obj in response["Contents"]:
            list.append(obj["Key"])
    else:
        print("バケット内にオブジェクトはありません。")
    logger.info({
        'action': 'success',
        'return': list
    })
    return list

list = s3list(boto3.client("s3"), 'u10.jp')
print(list)