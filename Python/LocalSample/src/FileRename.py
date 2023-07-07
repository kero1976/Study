"""
指定したフォルダ以下のファイルの一覧を取得し、一部のファイル名をリネームする
一括してバージョン番号を変更するのに使用する
"""
import os
import glob
from termcolor import colored

def execute():
    inputdir = input(colored("リネーム対象のフォルダパスを入力してください:", "blue"))
    if os.path.isdir(inputdir):
        files = filesarch(inputdir)
        oldname = input(colored("リネーム対象の変更前ファイル名を入力してください:", "blue"))
        newname = input(colored("リネーム対象の変更後ファイル名を入力してください:", "blue"))
        for file in files:
            renamename = rename(file, oldname, newname)
            if file == renamename:
                print(colored(f"[-]{file}", "green"))
            else:
                print(colored(f"[+]{file} -> {renamename}", "blue"))
                os.rename(file, renamename)
    else:
        print(colored("フォルダが見つかりませんでした。", "red"))


def rename(data, old, new):
    if old in data:
        return data.replace(old, new)
    else:
        return data
    

def filesarch(dir):
    files = glob.glob(dir + "/**/*")
    return files

if __name__ == "__main__":
    execute()