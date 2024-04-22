import OpenSSL.crypto
import cryptography.hazmat.primitives.serialization
from logging import getLogger
from certificateutil.file.file_writer import FileWriter

logger = getLogger(__name__)


class PrivateKeyCreate:

    @classmethod
    def create_rsa_key_with_password(
        cls, bits: int, cipher: str, password: bytes, file_path: str
    ) -> bool:
        """パスワード付きの秘密鍵(PEM形式)を作成する

        Args:
            bits (int): 鍵の長さ
            cipher (str): 暗号化アルゴリズム
            password (bytes): パスワード
            file_path (str): ファイルパス

        Returns:
            _type_: _description_
        """
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
        try:
            pk = OpenSSL.crypto.PKey()
            pk.generate_key(OpenSSL.crypto.TYPE_RSA, bits)

            # RSA秘密鍵をPEM形式でエクスポート
            private_key = OpenSSL.crypto.dump_privatekey(
                OpenSSL.crypto.FILETYPE_PEM,
                pk,
                cipher=cipher,
                passphrase=password,
            )

            FileWriter(file_path).write_binary(private_key)
            logger.debug({"action": "success", "return": True})
            logger.info(f"Create Private Encrypted Key Success.({file_path})")
            return True
        except Exception as e:
            logger.debug({"action": "fail", "exception": e})
            logger.error(f"Create Private Encrypted Key Failed.({file_path})")

    @classmethod
    def create_rsa_key(cls, bits, file_path: str):
        logger.debug(
            {
                "action": "start",
                "params": {
                    "bits": bits,
                    "file_path": file_path,
                },
            }
        )
        # 秘密鍵を生成
        pk = OpenSSL.crypto.PKey()
        pk.generate_key(OpenSSL.crypto.TYPE_RSA, bits)

        # RSA秘密鍵をPEM形式でエクスポート
        private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, pk)

        FileWriter(file_path).write_binary(private_key)
        logger.debug({"action": "success", "return": True})
        logger.info(f"Create Private Key Success.({file_path})")
        return True

    @classmethod
    def create_rsa_key_der(cls, bits, file_path: str):
        logger.debug(
            {
                "action": "start",
                "params": {
                    "bits": bits,
                    "file_path": file_path,
                },
            }
        )
        # 秘密鍵を生成
        pk = OpenSSL.crypto.PKey()
        pk.generate_key(OpenSSL.crypto.TYPE_RSA, bits)

        # RSA秘密鍵をPEM形式でエクスポート
        private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_ASN1, pk)

        FileWriter(file_path).write_binary(private_key)
        logger.debug({"action": "success", "return": True})
        logger.info(f"Create Private Key(DER) Success.({file_path})")
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
