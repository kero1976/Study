from logging import getLogger
from bs4 import BeautifulSoup

logger = getLogger(__name__)

def link_selection(html: str) -> list[(str, str)]:
    """HTMLファイルから画像リンク部分を抽出
    Args:
        html (str): _description_

    Returns:
        list[(str, str)]: (url, name)
    """
    logger.debug({"action": "start","param":html})
    soup = BeautifulSoup(html, "html.parser")
    imgs= soup.select("img")
    logger.debug({"action": "run","message": "parse img.", "size": len(imgs)})
    result = []
    for img in imgs:
        try:
            result.append((img['data-src'], img['alt']))
        except Exception as e:
            logger.debug({"action": "run", "message": "parse error", "value": img})
    
    logger.debug({'action': 'success', 'result': result})
    logger.info({'action': 'success'})
    return result

def next_url(html:str):
    soup = BeautifulSoup(html, "html.parser")
    a_tag= soup.select("a")
    print("a tag:")
    print(len(a_tag))
    nexts = soup.find_all(rel="next")
    for next in nexts:
        return next["href"]