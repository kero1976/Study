from OpenSSL import crypto
from os.path import join
from certificateutil.openssl.private.private_key_load import PrivateKeyLoad
from logging import getLogger
from OpenSSL.crypto import X509Name

logger = getLogger(__name__)


class CertificateCreater:

    @classmethod
    def create_cert(cls, private_key, certificate_file_path):
        """証明書（cert）を作成."""
        logger.debug(
            {
                "action": "start",
                "params": {
                    "private_key": private_key,
                    "certificate_file_path": certificate_file_path,
                },
            }
        )
        key = PrivateKeyLoad.load_rsa_key(private_key)
        # create self-signed cert
        cert = crypto.X509()
        # cert.get_subject().C = "JP"
        # cert.get_subject().ST = "A"
        # cert.get_subject().L = "B"
        # cert.get_subject().O = "C"
        # cert.get_subject().OU = "D"
        cert.get_subject().CN = "E"

        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)
        # cert.add_extensions(
        #     [
        #         crypto.X509Extension(
        #             "basicConstraints".encode("ascii"),
        #             False,
        #             "CA:FALSE".encode("ascii"),
        #         ),
        #         crypto.X509Extension(
        #             "keyUsage".encode("ascii"),
        #             True,
        #             "Digital Signature, Non Repudiation".encode("ascii"),
        #         ),
        #         crypto.X509Extension(
        #             "issuerAltName".encode("ascii"),
        #             False,
        #             "email:".encode("ascii") + "test".encode("ascii"),
        #         ),
        #     ]
        # )
        # v3
        cert.set_version(2)
        # self signature
        cert.sign(key, "sha256")

        # save cert
        open(certificate_file_path, "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8")
        )
        logger.debug({"action": "success", "return": True})
        logger.info(f"Create X509 Certificate Success.({certificate_file_path})")
        return True
