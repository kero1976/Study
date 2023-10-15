from file.fileutil import get_filename
import pytest

def test_get_filename_ok():
    file_name = get_filename("G:/本/セキュリティ/IPA/2023/yougoyashikumi_2023.pdf")
    assert file_name == "yougoyashikumi_2023.pdf"

def test_get_filename_ok2():
    file_name = get_filename("test_fileutil.py")
    assert file_name == "test_fileutil.py"

def test_get_filename_ng():
    with pytest.raises(ValueError) as e:
        get_filename("G:/本/セキュリティ/IPA/2023/yougoyashikumi_2023NG.pdf")
        
    # エラーメッセージを検証
    assert str(e.value) == r"ファイル(G:\本\セキュリティ\IPA\2023\yougoyashikumi_2023NG.pdf)が存在しない"

def test_get_filename_ng2():
    with pytest.raises(ValueError) as e:
        get_filename("test_fileutilNG.py")
    # エラーメッセージを検証
    assert str(e.value) == r"ファイル(F:\VSCODEProject\Study\Python\LocalSample\tests\unit\file\test_fileutilNG.py)が存在しない"


def test_get_filename_none():
    with pytest.raises(ValueError) as e:
        get_filename(None)
    # エラーメッセージを検証
    assert str(e.value) == "引数(None)の値が不正"


def test_get_filename_none():
    with pytest.raises(ValueError) as e:
        get_filename({"a": "a"})
    # エラーメッセージを検証
    assert str(e.value) == "引数({'a': 'a'})の値が不正"