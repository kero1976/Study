import os
from logging import getLogger, StreamHandler, DEBUG, Formatter, basicConfig

# ロガーの作成
logger = getLogger(__name__)

basicConfig(level=DEBUG, format="%(asctime)s:%(funcName)s:%(message)s")

# ログメッセージの出力
logger.debug("Debug レベルのログメッセージ")

def get_filename(filepath: str) -> str:
    """ファイル名の取得
    ファイルパスを指定し、ファイルが存在する場合は、ファイル名を返す

    Args:
        filepath (str): ファイルパス

    Returns:
        str: ファイル名
    """
    logger.debug({
        "action": "start",
        "param":{
            "filepath": filepath
        }
    })
    if type(filepath) is not str:
        logger.debug({
            "action": "fail",
            "param":{
                "filepath": filepath
            },
            "message": "引数の値が不正"
        })
        raise ValueError(f"引数({filepath})の値が不正")
    
    abspath = os.path.abspath(filepath)
    if os.path.isfile(abspath):
        basename = os.path.basename(abspath)
        logger.debug({
            "action": "success",
            "param":{
                "filepath": filepath
            },
            "return": basename
        })
        return basename
    else:
        logger.debug({
            "action": "fail",
            "param":{
                "filepath": filepath
            },
            "message": "ファイルが存在しない",
            "abspath": abspath
        })
        raise ValueError(f"ファイル({abspath})が存在しない")


