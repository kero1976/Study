from OpenSSL import crypto
from os.path import join
from certificateutil.openssl.private.private_key_load import PrivateKeyLoad
from logging import getLogger
from OpenSSL.crypto import X509Name
from certificateutil.file.file_reader import FileReader
import datetime
from dateutil.tz import gettz

logger = getLogger(__name__)


class X509CertificateLoad:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cert = None

    def load(self):
        logger.debug(
            {
                "action": "start",
            }
        )
        reader = FileReader(self.file_path)
        buffer = reader.read()
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, buffer)
        self.cert = cert
        logger.debug({"action": "success", "cert": cert})
        return cert

    def read_cerial_number(self) -> str:
        """シリアル番号
        Windowsと合わせて16進数で40桁表記とする

        Returns:
            str: _description_
        """
        logger.debug({"action": "start", "cert": self.cert})
        serial = self.cert.get_serial_number()
        result = f"{serial:040x}"
        logger.debug({"action": "success", "serial": serial, "result": result})
        return result

    def read_subject(self):
        logger.debug({"action": "start", "cert": self.cert})
        subject = self.cert.get_subject()
        issuer = self.cert.get_issuer()
        after = self.cert.get_notAfter()
        before = self.cert.get_notBefore()
        signature_algorithm = self.cert.get_signature_algorithm()
        # datetime_utc = datetime.datetime.strptime(after)
        # datetime_jst = datetime_utc.astimezone(gettz("Asia/Tokyo"))
        pubkey = self.cert.get_pubkey()
        logger.debug(f"subject:{subject}")
        logger.debug(f"issuer:{issuer}")
        logger.debug(f"after:{after}")
        logger.debug(f"before:{before}")
        logger.debug(f"signature_algorithm:{signature_algorithm}")
        logger.debug(f"pubkey:{pubkey}")
        # logger.info(self.cert.signature)
        # pubkey.verify(signature, cert.tbs_certificate_bytes, hashes[hash_algo])
