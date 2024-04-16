from logging import getLogger
import base64

logger = getLogger(__name__)

class Base64Decoder():
    
    @classmethod
    def decode(cls, str_data) -> bytes:
        """Base64データをデコードする

        Args:
            data (str): _description_
        """
        logger.debug({"action": "start", "params":{
            "str_data": str_data
        }})
        result = base64.b64decode(str_data)
        logger.debug({"action": "success"})
        return result