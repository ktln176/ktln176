from unittest import TestCase

from static.mysql_connection import MysqlConnection


class MysqlConnectionTest(TestCase):

    def test_connection(self):
        """测试连接和关闭mysql连接"""
        MysqlConnection.connection()

        MysqlConnection.cur.execute('use ktln176;')
        MysqlConnection.cur.execute('show tables;')
        res = MysqlConnection.cur.fetchall()
        print(res)

        MysqlConnection.close()
        pass
