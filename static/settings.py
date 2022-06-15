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

    @property
    def get_debug(self) -> bool:
        return self.__debug

    @property
    def get_host(self) -> str:
        return self.__host

    @property
    def get_port(self) -> int:
        return self.__port

    @property
    def get_mysql_host(self) -> str:
        return self.__mysql_host

    @property
    def get_mysql_port(self) -> int:
        return self.__mysql_port

    @property
    def get_mysql_user(self) -> str:
        return self.__mysql_user

    @property
    def get_mysql_password(self) -> str:
        return self.__mysql_password

    @property
    def get_redis_host(self) -> str:
        return self.__redis_host

    @property
    def get_redis_port(self) -> int:
        return self.__redis_port
