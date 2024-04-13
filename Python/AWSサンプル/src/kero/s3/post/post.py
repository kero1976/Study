from pathlib import Path

import boto3
import io
import os
from logging import getLogger
from urllib import parse

s3 = boto3.resource("s3")
bucket = s3.Bucket("kerodoc")
logger = getLogger(__name__)



def put_file_and_tag(bucket, file: str, tags: dict):
    bucket.upload_file(
        str(file), get_filename(file), ExtraArgs={"Tagging": parse.urlencode(tags)}
    )


def get_filename(filepath: str) -> str:
    """ファイル名の取得
    ファイルパスを指定し、ファイルが存在する場合は、ファイル名を返す

    Args:
        filepath (str): ファイルパス

    Returns:
        str: ファイル名
    """
    logger.debug({"action": "start", "param": {"filepath": filepath}})
    if type(filepath) is not str:
        logger.debug(
            {"action": "fail", "param": {"filepath": filepath}, "message": "引数の値が不正"}
        )
        raise ValueError(f"引数({filepath})の値が不正")

    abspath = os.path.abspath(filepath)
    if os.path.isfile(abspath):
        basename = os.path.basename(abspath)
        logger.debug(
            {"action": "success", "param": {"filepath": filepath}, "return": basename}
        )
        return basename
    else:
        logger.debug(
            {
                "action": "fail",
                "param": {"filepath": filepath},
                "message": "ファイルが存在しない",
                "abspath": abspath,
            }
        )
        raise ValueError(f"ファイル({abspath})が存在しない")


ORIGIN_PATH = "G:/ブラウザTemp/Oracle/S105684GC10JP-23_Design_for_Security_and_Compliance.pdf"
tags = {
    "name": "9.セキュリティとコンプライアンスの設計",
    "copyright": "Oracle", 
    # "publisher": "淵上　真一", 
    # "date": "2023",
    "filetype": "pdf",
    "category": "OCI",
    "public": True,
    "note": "Oracle Cloud Infrastructure 2023 Architect Professional",
    }
# print(tags)
put_file_and_tag(bucket, ORIGIN_PATH, tags)

