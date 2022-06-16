class Settings:
    def __init__(self):
        pass

    __debug: bool = True
    __host: str = '0.0.0.0'
    __port: int = 7070

    __mysql_host = '120.25.120.132'
    __mysql_port = 3306
    __mysql_user = 'root'
    __mysql_password = 'K4907tln__'

    __redis_host = '120.25.120.132'
    __redis_port = 6379

    @classmethod
    def get_debug(cls) -> bool:
        return cls.__debug

    @classmethod
    def get_host(cls) -> str:
        return cls.__host

    @classmethod
    def get_port(cls) -> int:
        return cls.__port

    @classmethod
    def get_mysql_host(cls) -> str:
        return cls.__mysql_host

    @classmethod
    def get_mysql_port(cls) -> int:
        return cls.__mysql_port

    @classmethod
    def get_mysql_user(cls) -> str:
        return cls.__mysql_user

    @classmethod
    def get_mysql_password(cls) -> str:
        return cls.__mysql_password

    @classmethod
    def get_redis_host(cls) -> str:
        return cls.__redis_host

    @classmethod
    def get_redis_port(cls) -> int:
        return cls.__redis_port
