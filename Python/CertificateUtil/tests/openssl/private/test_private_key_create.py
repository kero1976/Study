from certificateutil.openssl.private.private_key_create import PrivateKeyCreate
from certificateutil.file.file_reader import FileReader
import pytest


def test_create_all():
    dir = "tests/data/秘密鍵/"
    PrivateKeyCreate.create_rsa_key(2048, f"{dir}/private.pem")
    PrivateKeyCreate.create_rsa_key_with_password(
        2048, "aes-128-cbc", b"p@ssw0rd!", f"{dir}/private_password.pem"
    )
    PrivateKeyCreate.create_rsa_key_der(2048, f"{dir}/private.der")


def test_create_nonepassword_der(tmpdir):
    file1 = f"{tmpdir}/test1.key"
    assert PrivateKeyCreate.create_rsa_key_der(2048, file1) == True
    size = FileReader(file1).get_size()
    assert size > 1100
    assert size < 1300


def test_create_nonepassword(tmpdir):
    file1 = f"{tmpdir}/test1.key"
    assert PrivateKeyCreate.create_rsa_key(2048, file1) == True
    size = FileReader(file1).get_size()
    assert size > 1600
    assert size < 1800
    assert FileReader(file1).head(27) == "-----BEGIN PRIVATE KEY-----"

    file2 = f"{tmpdir}/test.key"
    assert PrivateKeyCreate.create_rsa_key(4096, file2) == True
    size = FileReader(file2).get_size()
    assert size > 3200
    assert size < 3300


def test_create_password(tmpdir):
    file1 = f"{tmpdir}/test1.key"
    assert (
        PrivateKeyCreate.create_rsa_key_with_password(
            2048, "aes-128-cbc", b"p@ssw0rd!", file1
        )
        == True
    )
    size = FileReader(file1).get_size()
    assert size > 1800
    assert size < 2000
    assert FileReader(file1).head(37) == "-----BEGIN ENCRYPTED PRIVATE KEY-----"

    file2 = f"{tmpdir}/test2.key"
    assert (
        PrivateKeyCreate.create_rsa_key_with_password(
            2048, "aes-256-cbc", b"p@ssw0rd!", file2
        )
        == True
    )
    size = FileReader(file2).get_size()
    assert size > 1800
    assert size < 2000
    assert FileReader(file2).head(37) == "-----BEGIN ENCRYPTED PRIVATE KEY-----"
