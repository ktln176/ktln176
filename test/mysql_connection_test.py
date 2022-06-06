from unittest import TestCase

from static.mysql_connection import MysqlConnection


class MysqlConnectionTest(TestCase):

    def test_connection(self):
        MysqlConnection.execute_sql('use ktln176;')
        MysqlConnection.execute_sql('show tables;')
