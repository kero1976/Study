from certificateutil.openssl.private.private_key_create import PrivateKeyCreate
from certificateutil.file.file_reader import FileReader
import pytest
from certificateutil.openssl.public.x509_certificate_create import CertificateCreater


@pytest.mark.kero
def test_sinario():
    dir = "./"
    print("ルート証明書の秘密鍵を作成")
    ca_password = f"{dir}/root_ca_private.pem"
    cakey = PrivateKeyCreate.create_rsa_key(2048, ca_password)

    print("ルート証明書を自己署名で作成")

    ca_cert = f"{dir}/ca.pem.cer"
    ca = CertificateCreater.create_cert(ca_password, ca_cert, "ca")

    print("子の証明書の秘密鍵を作成")
    web_password = f"{dir}/web_private.pem"
    PrivateKeyCreate.create_rsa_key(2048, web_password)

    # print("子の証明書をルート証明書で作成")
    # web_cert = f"{dir}/web.pem.cer"
    # CertificateCreater.create_cert_sign(web_password, web_cert, "web", cakey)
