from certificateutil.openssl.public.x509_certificate_create import CertificateCreater
import pytest


@pytest.mark.shijo
def test_load_rsa_key_with_password():
    file1 = "tests/data/秘密鍵/private.pem"
    file2 = "test.pem.cer"
    assert CertificateCreater.create_cert(file1, file2) is not None
