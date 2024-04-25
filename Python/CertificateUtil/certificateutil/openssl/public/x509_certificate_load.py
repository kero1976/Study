from OpenSSL import crypto
from os.path import join
from certificateutil.openssl.private.private_key_load import PrivateKeyLoad
from logging import getLogger
from OpenSSL.crypto import X509Name
from certificateutil.file.file_reader import FileReader

logger = getLogger(__name__)


class X509CertificateLoad:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        logger.debug(
            {
                "action": "start",
            }
        )
        reader = FileReader(self.file_path)
        buffer = reader.read()
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, buffer)
        logger.debug({"action": "success", "cert": cert})
        return cert
