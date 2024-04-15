from logging import getLogger
import os
import datetime
import json
from decimal import Decimal

logger = getLogger(__name__)

class FileWriter():
    """FileWriter
    テキストファイル・バイナリファイルを書き込むユーティリティクラス。
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None
    
    def write_text_utf8(self):
        logger.debug("start")
        with open(self.file_name, "w", encoding="utf-8") as f:
            f.write(self.data)
            
        logger.debug("end")
        
        
    def write_binary(self):
        logger.debug("start")
        with open(self.file_name, "wb") as f:
            f.write(self.data)
            
        logger.debug("end")