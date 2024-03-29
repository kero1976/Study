from dynamoutil.localfile.app import create_dir_file

def test_create_dir_file(tmpdir):
    assert create_dir_file("data1", ["a", "b"], tmpdir) is None