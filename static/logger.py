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

        # 1、创建一个logger
        cls.logger = logging.getLogger()  # 返回一个logger实例
        cls.logger.setLevel(logging.INFO)  # 设置logger级别为INFO

        # 2、创建一个handler,用于写入日志文件
        fh = logging.FileHandler(logging_file_path, mode='w')
        fh.setLevel(logging.INFO)

        # 3、再创建yig handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 4、定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 5、将logger添加到handler里面
        cls.logger.addHandler(fh)
        cls.logger.addHandler(ch)

    @classmethod
    def info(cls, text: str):
        if cls.logger is None:
            cls.init_logger()
        cls.logger.info(text)
