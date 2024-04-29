import OpenSSL.crypto as crypto
from datetime import datetime, timedelta

from logging import getLogger


# 自己署名のCA証明書を作成する関数
def create_ca_certificate():
    # 秘密鍵の生成
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # 証明書の作成
    cert = crypto.X509()
    cert.get_subject().CN = "Example CA"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 1 year validity
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.add_extensions(
        [
            crypto.X509Extension(b"basicConstraints", True, b"CA:TRUE, pathlen:0"),
            crypto.X509Extension(b"keyUsage", True, b"keyCertSign, cRLSign"),
            crypto.X509Extension(b"subjectKeyIdentifier", False, b"hash", subject=cert),
        ]
    )
    cert.sign(key, "sha256")

    # 秘密鍵と証明書をPEM形式でエンコード
    private_key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)
    cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)

    return private_key_pem, cert_pem


# 署名された証明書を作成する関数
def create_signed_certificate(ca_key_pem, ca_cert_pem):
    # CAの秘密鍵と証明書を読み込む
    ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, ca_key_pem)
    ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, ca_cert_pem)

    # 新しい秘密鍵の生成
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # 証明書の作成
    cert = crypto.X509()
    cert.get_subject().CN = "Example Certificate"
    cert.set_serial_number(2000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 1 year validity
    cert.set_issuer(ca_cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(ca_key, "sha256")

    # 証明書をPEM形式でエンコード
    cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)

    return cert_pem


# 自己署名のCA証明書を作成
ca_private_key_pem, ca_cert_pem = create_ca_certificate()

# CA証明書を表示
print("CA Certificate:")
print(ca_cert_pem.decode())

# CAの秘密鍵をファイルに保存
with open("ca_private_key.pem", "wb") as f:
    f.write(ca_private_key_pem)

# CA証明書をファイルに保存
with open("ca_certificate.pem.cer", "wb") as f:
    f.write(ca_cert_pem)

# 署名された証明書を作成
signed_cert_pem = create_signed_certificate(ca_private_key_pem, ca_cert_pem)

# 署名された証明書を表示
print("\nSigned Certificate:")
print(signed_cert_pem.decode())

# 署名された証明書をファイルに保存
with open("signed_certificate.pem,cer", "wb") as f:
    f.write(signed_cert_pem)
