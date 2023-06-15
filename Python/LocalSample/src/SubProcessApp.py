import subprocess
from logging import getLogger, StreamHandler, DEBUG, config
import os
config.fileConfig(os.path.join(os.path.dirname(__file__) , "./logging.ini"), encoding='utf-8')
logger = getLogger(__name__)


def call(execute: str):
    """
    同期呼び出し
    """
    logger.debug({"ACTION": "START",
                  "PARAM": str})


def asyncCall(execute: str):
    """
    非同期呼び出し
    """
    logger.debug({"ACTION": "START",
                  "PARAM": str})
    

if __name__ == "__main__":
    call("AAA")