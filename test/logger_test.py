import logging
from unittest import TestCase

from static.logger import Logger


class LoggingTest(TestCase):
    """logger 测试"""

    def test_logger(self):
        """测试写入日志文件类的调用"""
        Logger.info('hello')
        Logger.info('a')
        Logger.info('b')
        Logger.info('c')
    pass
