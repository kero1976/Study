from dynamoutil.localfile.file import create_file

def test_create_file(tmpdir):
    assert create_file("data1", ["a", "b"], tmpdir) == True