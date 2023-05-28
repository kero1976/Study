"""
S3にファイルがあるかどうかを確認する
"""

import boto3

# S3への接続
s3 = boto3.client("s3")

# バケット名
bucket_name = "u10.jp"

# バケット内のオブジェクトのリストを取得
response = s3.list_objects_v2(Bucket=bucket_name)

# オブジェクトのリストを表示
if "Contents" in response:
    for obj in response["Contents"]:
        print(obj["Key"])
else:
    print("バケット内にオブジェクトはありません。")
