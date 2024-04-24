from certificateutil.openssl.public.x509_certificate_create import CertificateCreater
import pytest
from certificateutil.openssl.private.private_key_load import PrivateKeyLoad


def test_create_cert(tmpdir):
    file1 = "tests/data/秘密鍵/private.pem"
    file2 = f"{tmpdir}/test.pem.cer"
    assert CertificateCreater.create_cert(file1, file2, "aaa") is not None


# @pytest.mark.shijo
# def test_create_cert_sign(tmpdir):
#     file1 = "tests/data/秘密鍵/private.pem"
#     file2 = f"./test.pem.cer"
#     keyfile = "tests/data/秘密鍵/private_password.pem"
#     key = PrivateKeyLoad.load_rsa_key_with_password(b"p@ssw0rd!", keyfile)
#     assert CertificateCreater.create_cert_sign(file1, file2, "aaa", key) is not None
