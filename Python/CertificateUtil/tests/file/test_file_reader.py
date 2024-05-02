import tempfile
import shutil
from certificateutil.file.file_reader import FileReader
import pytest


def test_read_create_read():
    """ファイルを作成して読み込む"""
    with tempfile.TemporaryDirectory() as temp_dir:
        testfile = f"{temp_dir}/test.txt"
        with open(testfile, mode="w") as f:
            f.write("Hello")

        file1 = FileReader(testfile)
        assert file1.read() == "Hello"


def test_read_copy_read(tmpdir):
    """ファイルをコピーして読み込む"""
    shutil.copytree("tests/data/", f"{tmpdir}/data")
    file1 = FileReader(f"{tmpdir}/data/テスト.txt")
    assert file1.read() == "テスト"
    file2 = FileReader(f"{tmpdir}/data/SJIS.txt")
    assert file2.read() == "これはSJISです"
    file3 = FileReader(f"{tmpdir}/data/googlelogo.png")
    assert file3.read() is not None
