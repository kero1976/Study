from logging import getLogger

from awspython.common.connection import Connection

logger = getLogger(__name__)


def list_tables(conn: Connection):
    logger.debug(f"start({conn=})")
    resource = conn.get_resource("dynamodb")
    tables = resource.tables.all()
    result = []
    for table in tables:
        result.append(table.table_name)

    return result
