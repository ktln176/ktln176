import redis

from static.settings import Settings


class RedisConnection:
    conn: redis.client.Redis = None

    @classmethod
    def connection(cls):
        """连接Redis"""
        pool = redis.ConnectionPool(decode_responses=True)
        cls.conn = redis.Redis(
            host=Settings.get_redis_host(),
            port=Settings.get_redis_port(),
            password=Settings.get_redis_password(),
            connection_pool=pool
        )

    @classmethod
    def close(cls):
        """关闭连接"""
        cls.conn.close()
