import pymysql
from static.settings import Settings
from unittest import TestCase


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
            database=Settings.get_mysql_database(),
            charset='utf8'
        )
        cls.cur = cls.conn.cursor()

    @classmethod
    def execute_sql(cls, sql: str):
        """
        执行SQL
        :param sql:
        :return:
        """
        if cls.conn is None:
            cls.connection()
        else:
            cls.cur.execute(sql)
            res = cls.cur.fetchall()
            print(res)
            cls.close()
            return res

    @classmethod
    def close(cls):
        """关闭mysql连接"""
        cls.conn.close()


class MysqlConnectionTest(TestCase):

    @staticmethod
    def test_connection():
        MysqlConnection.execute_sql('show tables;')
