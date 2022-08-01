import re

import requests


class Settings:
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
        ip = None
        try:
            res = requests.get('https://myip.ipip.net', timeout=5).text
            ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', res)
            ip = ip[0] if ip else ''
        except Exception:
            pass

        # 除了云环境，全部开启debug
        if ip == '120.25.120.132':
            return False
        else:
            return True

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
