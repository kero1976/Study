from src.FileRename import rename

def testRename1():
    assert rename("ABCDEFG", "X", "Z") == "ABCDEFG"

def testRename2():
    assert rename("ABCDEFG", "A", "Z") == "ZBCDEFG"

def testRename2():
    assert rename("ABCDEFG", "AB", "Z") == "ZCDEFG"