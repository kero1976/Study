from logging import getLogger
import os
import datetime
import json

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
            f.write(json.dumps(data))
    return True

def create_data_file(table_name: str, datas: list[dict], dir: str=None) -> bool:
    """_summary_

    Args:
        datas (list[dict]): _description_
        dir (str, optional): _description_. Defaults to None.

    Returns:
        bool: _description_
    """
    logger.debug(f"create_data_file start(table_name={table_name}, dir={dir})")
    file_name = f'{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}_{table_name}.json'
    return create_file(file_name, datas, dir)