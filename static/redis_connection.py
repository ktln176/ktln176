import redis
from static.settings import Settings


class RedisConnection:

    pool: redis.connection.ConnectionPool = None
    conn: redis.client.Redis = None

    @classmethod
    def connection(cls):
        """连接Redis"""
        cls.pool = redis.ConnectionPool(
            host=Settings.get_redis_host(),
            port=Settings.get_redis_port(),
            decode_responses=True
        )
        cls.conn = redis.Redis(connection_pool=cls.pool)
