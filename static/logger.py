import logging
import os


class Logger:
    """日志类"""
    logger = None

    @classmethod
    def init_logger(cls):
        # 当前文件路径
        self_file_path = os.path.abspath(__file__)

        # logger.log 日志文件保存位置
        logging_file_path = os.path.abspath(os.path.join(self_file_path, '..', 'log', 'logger.log'))

        # 第一步：创建日志器对象，默认等级为INFO
        cls.logger = logging.getLogger()
        logging.basicConfig(level=logging.INFO)

        # 第二步：创建控制台日志处理器+文件日志处理器
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(logging_file_path, mode="a", encoding="utf-8")

        # 第三步：设置控制台日志的输出级别,需要日志器也设置日志级别为info；----根据两个地方的等级进行对比，取日志器的级别
        console_handler.setLevel(level=logging.INFO)

        # 第四步：设置控制台日志和文件日志的输出格式
        console_fmt = "%(levelname)s -> %(asctime)s -> %(message)s"

        fmt1 = logging.Formatter(fmt=console_fmt)
        fmt2 = logging.Formatter(fmt=console_fmt)

        console_handler.setFormatter(fmt=fmt1)
        file_handler.setFormatter(fmt=fmt2)

        # 第五步：将控制台日志器、文件日志器，添加进日志器对象中
        cls.logger.addHandler(console_handler)
        cls.logger.addHandler(file_handler)

    @classmethod
    def info(cls, text: str):
        if cls.logger is None:
            cls.init_logger()
        cls.logger.info(text)
