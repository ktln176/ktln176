import pymysql

from static.settings import Settings


class MysqlConnection:

    conn: pymysql.connections.Connection = None
    cur: pymysql.cursors.Cursor = None

    @classmethod
    def connection(cls):
        """连接mysql"""
        cls.conn = pymysql.connect(
            host=Settings.get_mysql_host(),
            port=Settings.get_mysql_port(),
            user=Settings.get_mysql_user(),
            password=Settings.get_mysql_password(),
            charset='utf8'
        )
        cls.cur = cls.conn.cursor()

    @classmethod
    def close(cls):
        """关闭mysql连接"""
        cls.conn.close()
