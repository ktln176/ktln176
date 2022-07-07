import socket
from unittest import TestCase

import requests


class TestAll(TestCase):

    def test_1(self):
        # 获取本机计算机名称
        hostname = socket.gethostname()
        print(hostname)
        # 获取本机ip
        ip = socket.gethostbyname(hostname)
        print(ip)

    def test_2(self):
        ip = requests.get('https://checkip.amazonaws.com').text.strip()
        print(type(ip), len(ip), ip)
        pass
