from dynamoutil.localfile.file import create_file, create_data_file

def test_create_file(tmpdir):
    assert create_file("data1", ["a", "b"], tmpdir) == True
    
def test_create_data_file(tmpdir):
    assert create_data_file("data1", ["a", "b"], tmpdir) == True