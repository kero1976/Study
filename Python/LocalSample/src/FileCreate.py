from stopwatch import StopWatch
import SubProcessApp
import os



def createfile(typesize:str, name:str):
    createsize = _getsize(typesize)

    cmd = f"fsutil file createnew {name} {createsize}"
    SubProcessApp.call(cmd)

def createfile2(typesize:str, name:str):
    createsize = _getsize(typesize)
    with open(name, 'wb') as f:
        rand = os.urandom(createsize)
        f.write(rand)

def _getsize(typesize: str) -> int:
    (type, size) = typesize.split(",")
    if type == "K":
        return int(size) * 1024
    elif type == "M":
        return int(size) * 1024 * 1024
    elif type == "G":
        return int(size) * 1024 * 1024 * 1024
    else:
        return int(size)

if __name__ == "__main__":
    watch = StopWatch()
    # createfile("M,100", "100M")
    createfile2("M,100", "100M")
    print(watch.stop())