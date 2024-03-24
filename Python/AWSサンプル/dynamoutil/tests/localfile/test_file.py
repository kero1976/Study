from dynamoutil.localfile.file import create_file

def test_create_file():
    assert create_file(None, None) == True