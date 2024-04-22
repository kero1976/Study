import OpenSSL.crypto
import cryptography.hazmat.primitives.serialization
from logging import getLogger
from certificateutil.file.file_reader import FileReader

logger = getLogger(__name__)


class PrivateKeyLoad:

    @classmethod
    def load_rsa_key_with_password(cls, password: bytes, file_path: str) -> bool:
        """パスワード付きの秘密鍵(PEM形式)を読み込む

        Args:
            password (bytes): パスワード
            file_path (str): ファイルパス

        Returns:
            _type_: _description_
        """
        logger.debug(
            {
                "action": "start",
                "params": {
                    "password": password,
                    "file_path": file_path,
                },
            }
        )
        try:
            reader = FileReader(file_path)
            buffer = reader.read()

            # PEM形式のRSA秘密鍵を読み込む
            private_key = OpenSSL.crypto.load_privatekey(
                OpenSSL.crypto.FILETYPE_PEM,
                buffer,
                passphrase=password,
            )
            if private_key.type() == OpenSSL.crypto.TYPE_RSA:
                key_type = "RSA"
            elif private_key.type() == OpenSSL.crypto.TYPE_DSA:
                key_type = "DSA"
            else:
                key_type = "unknown"
            logger.debug(
                {
                    "action": "run",
                    "private_key": {
                        "bits": private_key.bits(),
                        "check": private_key.check(),
                        "type": f"{key_type}({private_key.type()})",
                    },
                }
            )
            rsa_private_key = private_key.to_cryptography_key()
            rsa_private_numbers = rsa_private_key.private_numbers()
            rsa_public_key = rsa_private_key.public_key()

            logger.debug(
                {
                    "action": "run",
                    "rsa_private_key": {
                        "d": rsa_private_numbers.d,
                        "dmp1": rsa_private_numbers.dmp1,
                        "dmq1": rsa_private_numbers.dmq1,
                        "iqmp": rsa_private_numbers.iqmp,
                        "p": rsa_private_numbers.p,
                        "public_numbers": rsa_private_numbers.public_numbers,
                        "q": rsa_private_numbers.q,
                    },
                }
            )

            logger.debug(dir(rsa_public_key))

            logger.debug({"action": "success", "return": True})
            logger.info(f"Load Private Encrypted Key Success.({file_path})")
            return True
        except Exception as e:
            logger.debug({"action": "fail", "exception": e})
            logger.error(f"Load Private Encrypted Key Failed.({file_path})")
