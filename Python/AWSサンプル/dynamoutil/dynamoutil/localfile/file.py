from logging import getLogger
import os
import datetime


logger = getLogger(__name__)

def create_file(file_name: str, datas: list[dict], dir: str=None) -> bool:
    """ファイルを作成する

    Args:
        file_name (str): ファイル名
        data (_type_): データ
        dir (str): フォルダ

    Returns:
        bool: True:ファイル作成成功、False:ファイル作成失敗
    """
    logger.debug(f"create_file start(file_name={file_name}, dir={dir})")
    if dir:
        path = f"{dir}/{file_name}"
    else:
        path = f"./{file_name}"
    logger.debug(f"path={os.path.abspath(path)}")
    
    with open(path, mode="w") as f:
        for data in datas:
            f.write(data)
    return True