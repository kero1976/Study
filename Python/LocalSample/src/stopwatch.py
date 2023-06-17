import time


class StopWatch():
    def __init__(self):
        self.__start = time.time()
        self.__stoplist = []

    def cleat(self):
        self.__stoplist.clear()
        self.__start = time.time()

    def stop(self):
        stop = time.time()
        self.__stoplist.append(stop)
        exectime = stop - self.__start
        return f'開始からの処理時間:{exectime:.2f}秒'

    def print(self):
        for i in self.__stoplist:
            exectime = i - self.__start
            print(f'開始からの処理時間:{exectime:.2f}秒')