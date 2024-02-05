from logging import getLogger,config
import os
from imagedownload.httprequest import request_response, get_dirname
from imagedownload.htmlparse import link_selection, next_url
from imagedownload.download import image_download
config.fileConfig(
    os.path.join(os.path.dirname(__file__), "logging.ini"), encoding="utf-8"
)
logger = getLogger(__name__)

def execute(url, fix):
    logger.info("START")
    while True:
        dirname = get_dirname(url, fix)
        html = request_response(url)
        links = link_selection(html)
        for (imageurl, name) in links:
            image_download(dirname, imageurl, name)
            
        next = next_url(html)
        if next is None:
            logger.info("END")
            return
        else:
            url = next
            