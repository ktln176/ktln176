import socket
from unittest import TestCase


class TestAll(TestCase):

    def test_1(self):
        # 获取本机计算机名称
        hostname = socket.gethostname()
        # 获取本机ip
        ip = socket.gethostbyname(hostname)
        print(ip)

    def test_2(self):
        pass
