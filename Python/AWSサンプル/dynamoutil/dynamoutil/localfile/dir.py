from logging import getLogger
import os
import datetime


logger = getLogger(__name__)

def create_dir(dir_name: str, work_dir: str=None) -> str:
    """指定した場所に指定した名前でフォルダを作成する
    work_dirを指定しなかった場合は、カレントディレクトリに作成する。
    Args:
        dir_name (_type_): フォルダ名
        work_dir (str): フォルダを作成する場所
    Returns:
        作成したフォルダパス。作成失敗時はNone
    """
    logger.debug(f"create_dir start(dir_name={dir_name}, work_dir={work_dir})")
    if ":" in dir_name:
        logger.error(f"create_dir fail.file_name in ':'.")
        return None
    if work_dir:
        path = f"{work_dir}/{dir_name}"
    else:
        path = f"./{dir_name}"
    abs_path = os.path.abspath(path)
    logger.debug(f"path={path}, abs_path={abs_path}")
    try:
        os.makedirs(abs_path, exist_ok=True)
        logger.debug(f"create_dir success.({abs_path})")
        return abs_path
    except Exception as e:
        logger.error(f"create_dir fail.{e}")
        return None
    
def create_date_dir(work_dir: str=None) -> str:
    """日付のフォルダ(YYYYMMDD)を作成する

    Args:
        work_dir (str, optional): _description_. Defaults to None.

    Returns:
        作成したフォルダパス
    """
    logger.debug(f"create_date_dir start(work_dir={work_dir})")
    date = f'{datetime.date.today():%Y%m%d}'
    return create_dir(date, work_dir)
