from dynamoutil.localfile.dir import create_dir, create_date_dir
import os
import pytest

def test_create_dir_ok1(tmpdir):
    assert create_dir("xyz") == True

@pytest.mark.shijo
def test_create_dir_ok2(tmpdir):
    assert create_dir("xyz", tmpdir) == True
    
def test_create_dir_ng1():
    assert create_dir("C:/abc", "xyz") == False
    assert create_dir("abc", "C:/abc") == False

def test_create_dir_ng2():
    assert create_dir("C:/abc", "xyz") == False
    assert create_dir("abc", "C:/abc") == False
      
def test_create_date_dir():
    assert create_date_dir("C:/abc") == True
    assert create_date_dir() == True

