from logging import getLogger,config
import os
import urllib.parse
import requests


config.fileConfig(
    os.path.join(os.path.dirname(__file__), "logging.ini"), encoding="utf-8"
)
logger = getLogger(__name__)

def request_response(url: str) -> dict:
    """リクエストのURLを送信し、その結果を取得する

    Args:
        url (str): _description_

    Returns:
        dict: _description_
    """
    logger.debug({"action": "start","param": url, "url": urllib.parse.unquote(url, "utf-8")})
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug({"action": "success", "response": response.text})
        return response.text
    else:
        logger.debug({"action": "fail", "status_code": response.status_code})
        
        
logger.debug("AAA")
print("ABC")

response = request_response("https://www.google.com")
print(response)