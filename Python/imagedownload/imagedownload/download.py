from logging import getLogger
import cloudscraper
import os
import urllib.parse

logger = getLogger(__name__)

def image_download(dirname, url, name):
    logger.debug({"action": "start","url":url, "name": name})
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        "referer": "https://mangaraw.to/"
    }
    scraper = cloudscraper.create_scraper()

    response = scraper.get(url, headers=headers)
    filename = get_file_name(dirname, url, name)
    save_image(filename, response.content)
    
def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)
        
def get_file_name(dirname, url, name):
    """_summary_

    Args:
        url (_type_): ファイル名
        name (_type_): URLから拡張子を取得
    """
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    
    return os.path.join(dirname, name + url[url.rfind("."):])

