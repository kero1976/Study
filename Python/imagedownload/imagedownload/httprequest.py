from logging import getLogger
import os
import urllib.parse
import requests

logger = getLogger(__name__)

def request_response(url: str) -> str:
    """リクエストのURLを送信し、その結果を取得する

    Args:
        url (str): リクエストURL

    Returns:
        str: response.text
    """
    logger.debug({"action": "start","param": url, "url": urllib.parse.unquote(url, "utf-8")})
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.debug({"action": "success", "response": response.text})
            logger.info({"action": "success"})
            return response.text
        else:
            logger.debug({"action": "fail", "status_code": response.status_code})
    except Exception as e:
        logger.error({
            "action": "fail",
            "type": type(e),
            "url": url
        })
        
def get_dirname(url, fix):
    data = url[len(fix):]
    return urllib.parse.unquote(data, "utf-8").replace("/","")