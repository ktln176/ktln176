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

    @classmethod
    def info(cls, text: str):
        if cls.logger is None:
            cls.init_logger()
        cls.logger.info(text)
