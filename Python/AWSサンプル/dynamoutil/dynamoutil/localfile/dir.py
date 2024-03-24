from logging import getLogger
import os
import datetime


logger = getLogger(__name__)

def create_dir(dir_name: str, work_dir: str=None) -> bool:
    """指定した場所に指定した名前でフォルダを作成する
    work_dirを指定しなかった場合は、カレントディレクトリに作成する。
    Args:
        dir_name (_type_): フォルダ名
        work_dir (str): フォルダを作成する場所
    Returns:
        bool: True:フォルダ作成成功、False:フォルダ作成失敗
    """
    logger.debug(f"create_dir start(dir_name={dir_name}, work_dir={work_dir})")
    if work_dir:
        path = f"{work_dir}/{dir_name}"
    else:
        path = f"./{dir_name}"
    logger.debug(f"path={os.path.abspath(path)}")
    try:
        os.makedirs(path, exist_ok=True)
        logger.debug(f"create_dir success.({path})")
        return True
    except Exception as e:
        logger.error(f"create_dir fail.{e}")
        return False
    
def create_date_dir(work_dir: str=None) -> bool:
    """日付のフォルダ(YYYYMMDD)を作成する

    Args:
        work_dir (str, optional): _description_. Defaults to None.

    Returns:
        bool: True:フォルダ作成成功、False:フォルダ作成失敗
    """
    logger.debug(f"create_date_dir start(work_dir={work_dir})")
    date = f'{datetime.date.today():%Y%m%d}'
    return create_dir(date, work_dir)
