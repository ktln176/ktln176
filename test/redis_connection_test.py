from unittest import TestCase

from static.database.redis_connection import RedisConnection


class RedisConnectionTest(TestCase):

    def test_connection(self):
        """测试连接和关闭redis连接"""
        RedisConnection.connection()

        RedisConnection.conn.set('key1', 'value1')
        val = RedisConnection.conn.get('key1')
        print(val)

        RedisConnection.close()
        pass
