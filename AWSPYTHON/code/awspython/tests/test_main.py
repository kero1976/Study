from awspython.common.connection import Connection
from awspython.dynamodb.list_table import list_tables


def test_main():
    conn = Connection()

    result = list_tables(conn)
    print("◇" * 100)
    print(result)
