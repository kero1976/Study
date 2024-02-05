from filereader.file_reader import FileReader
import pytest

def test_read_ok():
    assert FileReader("test.txt").read() is not None
    assert FileReader("UTF8.txt").read() is not None
    assert FileReader("SJIS.txt").read() is not None
    
    
def test_read_ok_utf8():
    reader = FileReader("UTF8.txt")
    result = reader._read_utf8()
    assert result is True
    
def test_read_ng_utf8():
    reader = FileReader("SJIS.txt")
    result = reader._read_utf8()
    assert result is False
    
def test_read_ok_cp932():
    reader = FileReader("SJIS.txt")
    result = reader._read_cp932()
    assert result is True
    
def test_read_ng_cp932():
    reader = FileReader("UTF8.txt")
    result = reader._read_cp932()
    assert result is False
    
def test_read_ng():
    reader = FileReader("test2.txt")
    with pytest.raises(ValueError):
        result = reader.read()

@pytest.mark.skip
def test_read_ok_image():
    reader = FileReader("画像.jpeg")
    result = reader.read()
    assert result is not None
    
@pytest.mark.shijo
def test_read_bin():
    # reader = FileReader("画像.jpeg")
    reader = FileReader("binary2.bin")
    reader._read_binary()
    print(reader.file_data)

   
# @pytest.mark.shijo 
# def test_file_create():
#     with open('binary2.bin', 'wb') as f:
#         for i in range(256):
#             for j in range(256):
#                 f.write(i.to_bytes())
#                 f.write(j.to_bytes())