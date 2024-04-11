from logging import getLogger
from .dir import create_date_dir
from .file import create_data_file

logger = getLogger(__name__)

def create_dir_file(table_name: str, datas: list, dir=None) -> str:
    """年月日フォルダを作成し、その下に年月日時分秒ファイルを作成する

    Args:
        table_name (str): _description_
        datas (list): _description_
    """
    logger.info(f"create_dir_file start(table_name={table_name}, dir={dir})")
    sub_dir = create_date_dir(dir)
    if sub_dir:
        result = create_data_file(table_name, datas, sub_dir)
        if result:
            logger.info("success")
    else:
        logger.error("create_dir_file fail.(sub dir create fail.)")
        return None
