from certificateutil.openssl.private.private_key_load import PrivateKeyLoad
from certificateutil.file.file_reader import FileReader
import pytest


def test_load_rsa_key_with_password():
    file1 = "tests/data/秘密鍵/private_password.pem"
    assert PrivateKeyLoad.load_rsa_key_with_password(b"p@ssw0rd!", file1) is not None


@pytest.mark.shijo
def test_load_rsa_key():
    file1 = "tests/data/秘密鍵/private.pem"
    assert PrivateKeyLoad.load_rsa_key(file1) is not None
