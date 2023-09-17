from binary.filereader import getbytedates

BASE_DIR = "F:/VSCODEProject/Study/Python/LocalSample/tests/unit/testdata"

def test_getbytedates_ng():
    assert None == getbytedates("HOGE")


def test_getbytedates_data1():
    result = getbytedates(BASE_DIR + "/data2")
    print(type(result))
    assert result is not None