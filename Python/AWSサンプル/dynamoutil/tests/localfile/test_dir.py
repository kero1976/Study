from dynamoutil.localfile.dir import create_dir, create_date_dir
import os
import pytest


def test_create_dir_ok1(tmpdir):
    """一時フォルダに移動して、カレントフォルダにフォルダを作成。成功"""
    os.chdir(tmpdir)
    assert create_dir("xyz") == True

def test_create_dir_ok2(tmpdir):
    """指定した一時フォルダにフォルダを作成。成功"""
    assert create_dir("xyz", tmpdir) == True
    
def test_create_dir_ng1(tmpdir):
    """一時フォルダに移動して、カレントフォルダにフォルダを作成。失敗"""
    os.chdir(tmpdir)
    assert create_dir("C:/abc") == False
    with open("xyz","w"):pass
    assert create_dir("xyz") == False

def test_create_dir_ng2(tmpdir):
    assert create_dir("C:/abc", tmpdir) == False
    with open(f"{tmpdir}/xyz","w"):pass
    assert create_dir("xyz", tmpdir) == False
      
def test_create_date_dir():
    assert create_date_dir("C:/abc") == True
    assert create_date_dir() == True

