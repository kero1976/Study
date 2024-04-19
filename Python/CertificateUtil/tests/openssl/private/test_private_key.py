from certificateutil.openssl.private.private_key import PrivateKey
from certificateutil.file.file_reader import FileReader
import pytest


@pytest.mark.shijo
def test_create(tmpdir):
    file1 = f"{tmpdir}/test1.key"
    assert PrivateKey.rsa_create(2048, file1) == True
    size = FileReader(file1).get_size()
    assert size > 1500
    assert size < 2500
    assert FileReader(file1).head(27) == "-----BEGIN PRIVATE KEY-----"

    file2 = f"{tmpdir}/test.key"
    assert PrivateKey.rsa_create(4096, file2) == True
    size = FileReader(file2).get_size()
    assert size > 2500
    assert size < 4000
