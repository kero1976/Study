from logging import getLogger
import os

logger = getLogger(__name__)


def getbytedates(filepass: str) -> bytes:
    """指定したファイルの内容をバイナリで取得する

    Args:
        filepass (_type_): ファイルパス

    Returns:
        bytes: ファイルの内容
    """
    logger.debug({
        "action": "start",
        "param": filepass
    })
    is_file = os.path.isfile(filepass)
    if is_file:
        with open(filepass, "rb") as f:
            result = f.read()
            logger.debug({
                "action": "success",
                "param": filepass,
                "message": "data size is {:,} byte.".format(len(result))
            })
            return result
    else:
        logger.debug({
            "action": "fail",
            "param": filepass,
            "message": "file is not found.{}".format(os.path.abspath(filepass))
        })
        return None
    