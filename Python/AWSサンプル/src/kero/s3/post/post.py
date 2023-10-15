from pathlib import Path

import boto3
import io
import os
from logging import getLogger
from urllib import parse

s3 = boto3.resource("s3")
bucket = s3.Bucket("kerodoc")
logger = getLogger(__name__)

KEY = "yougoyashikumi_2023.pdf"


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


ORIGIN_PATH = "G:/本/セキュリティ/IPA/2023/yougoyashikumi_2023.pdf"
tags = {"mykey": "myvalue", "mykey2": "myvalue2", "mykey2": "myvalue2", "mykey2": "myvalue2", "mykey2": "myvalue2", "mykey2": "myvalue2", "mykey2": "myvalue2"}
put_file_and_tag(bucket, ORIGIN_PATH, tags)
