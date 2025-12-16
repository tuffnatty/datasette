from datasette import hookimpl
from datasette.utils.sqlite import sqlite3


@hookimpl
def prepare_connection(conn):
    if hasattr(conn, "setconfig"):
        # Available only since Python 3.12
        conn.setconfig(sqlite3.SQLITE_DBCONFIG_DQS_DDL, False)
        conn.setconfig(sqlite3.SQLITE_DBCONFIG_DQS_DML, False)
