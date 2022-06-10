from unittest import TestCase

from static.mysql_connection import MysqlConnection


class MysqlConnectionTest(TestCase):

    def test_connection(self):
        """测试连接和关闭mysql连接"""
        MysqlConnection.connection()

        MysqlConnection.cur.execute('use ktln176;')
        sql = "select * from resume;"
        MysqlConnection.cur.execute(sql)
        res = MysqlConnection.cur.fetchall()
        print(res)

        MysqlConnection.close()
        pass
