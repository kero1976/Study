import OpenSSL.crypto
import cryptography.hazmat.primitives.serialization
from logging import getLogger
from certificateutil.file.file_writer import FileWriter

logger = getLogger(__name__)


class PrivateKey:

    @classmethod
    def rsa_create(cls, bits: int, file_path: str):
        """RSA形式の秘密鍵を作成する

        Args:
            bits (int): 暗号化ビット数
            file_path (str): 出力ファイルパス
        """

        logger.debug({"action": "start"})
        key_type = OpenSSL.crypto.TYPE_RSA
        pk = OpenSSL.crypto.PKey()
        pk.generate_key(key_type, bits)
        key = pk.to_cryptography_key()

        # 秘密鍵をPEMエンコーディングで出力
        encoding = cryptography.hazmat.primitives.serialization.Encoding.PEM
        # PEMエンコーディング
        format = cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8
        # PKCS #8 形式
        encryption_algorithm = (
            cryptography.hazmat.primitives.serialization.NoEncryption()
        )
        pem = key.private_bytes(encoding, format, encryption_algorithm)

        # ファイルに保存
        FileWriter(file_path).write_binary(pem)

        logger.debug({"action": "success", "return": True})
        return True
