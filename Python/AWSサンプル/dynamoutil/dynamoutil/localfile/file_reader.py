from logging import getLogger, StreamHandler, DEBUG, Formatter, basicConfig
import os

# ロガーの作成
logger = getLogger(__name__)

# ログメッセージの出力

class FileReader():
    """FileReader
    テキストファイル・バイナリファイルを読み込むユーティリティクラス。
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_data = None
        
    def read(self):
        logger.debug("start")
        self.get_filename(self.file_name)
        if self.file_data is None:
            if not self._read_utf8():
                self._read_cp932()
                
        logger.debug({
            "action": "success",
            "result": self.file_data
        })
        return self.file_data
    
    def _read_utf8(self) -> bool:
        """文字コードをUTF-8としてファイルを読み込む

        Returns:
            bool: True:ファイル読み込み成功、False:ファイル読み込み失敗
        """
        logger.debug({"action": "start"})
        try:
            with open(self.file_name, 'r', encoding="utf-8") as f:
                self.file_data = f.read()
                logger.debug({"action": "success"})
                return True
        except UnicodeDecodeError as e:
            logger.debug({"action": "fail"})
            return False
        
    def _read_cp932(self) -> bool:
        """文字コードをCP932としてファイルを読み込む

        Returns:
            bool: True:ファイル読み込み成功、False:ファイル読み込み失敗
        """
        logger.debug({"action": "start"})
        try:
            with open(self.file_name, 'r', encoding="cp932") as f:
                self.file_data = f.read()
                logger.debug({"action": "success"})
                return True
        except UnicodeDecodeError as e:
            logger.debug({"action": "fail"})
            return False
    
    def _read_binary(self) -> bool:
        """バイナリとしてファイルを読み込む

        Returns:
            bool: True:ファイル読み込み成功、False:ファイル読み込み失敗
        """
        logger.debug({"action": "start"})
        try:
            with open(self.file_name, 'rb') as f:
                self.file_data = f.read()
                logger.debug({"action": "success"})
                return True
        except UnicodeDecodeError as e:
            logger.debug({"action": "fail"})
            return False
            
    @classmethod
    def get_filename(cls, filepath: str) -> str:
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


