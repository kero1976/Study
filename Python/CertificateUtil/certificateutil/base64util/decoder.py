from logging import getLogger
import base64

logger = getLogger(__name__)

class Base64Decoder():
    
    @classmethod
    def decode(cls, str_data: str) -> bytes:
        """Base64データをデコードする

        Args:
            data (str): _description_
        """

        return base64.b64decode(str_data.encode())