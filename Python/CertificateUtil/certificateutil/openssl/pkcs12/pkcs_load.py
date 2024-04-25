from logging import getLogger

logger = getLogger(__name__)


class Pkcs12Load:
    def __init__(self, file_path):
        self.file_path = file_path
