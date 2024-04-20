import OpenSSL.crypto
import cryptography.hazmat.primitives.serialization
from logging import getLogger
from certificateutil.file.file_writer import FileWriter

logger = getLogger(__name__)


class PrivateKey:

    @classmethod
    def create_rsa_key_with_password(cls, bits, cipher, password, file_path: str):
        logger.debug(
            {
                "action": "start",
                "params": {
                    "bits": bits,
                    "cipher": cipher,
                    "password": password,
                    "file_path": file_path,
                },
            }
        )
        key_type = OpenSSL.crypto.TYPE_RSA

        # 秘密鍵を生成
        pk = OpenSSL.crypto.PKey()
        pk.generate_key(key_type, bits)

        # RSA秘密鍵をPEM形式でエクスポート
        private_key = OpenSSL.crypto.dump_privatekey(
            OpenSSL.crypto.FILETYPE_PEM, pk, cipher=cipher, passphrase=password
        )

        FileWriter(file_path).write_binary(private_key)
        logger.debug({"action": "success", "return": True})
        return True

    @classmethod
    def rsa_create(cls, bits: int, file_path: str):
        """RSA形式の秘密鍵を作成する

        Args:
            bits (int): 暗号化ビット数
            file_path (str): 出力ファイルパス
        """

        logger.debug(
            {
                "action": "start",
                "params": {
                    "bits": bits,
                    "file_path": file_path,
                },
            }
        )
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
