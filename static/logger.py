import logging
from logging import handlers


class Logger:
    logger: logging.RootLogger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:

            # 创建一个logger并设置日志等级
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)

            # 定义日志文件
            logFile = './log/logging.log'

            # 创建一个FileHandler,并将日志写入指定的日志文件中
            fileHandler = logging.FileHandler(logFile, mode='a')
            fileHandler.setLevel(logging.INFO)

            # 或者创建一个StreamHandler,将日志输出到控制台
            streamHandler = logging.StreamHandler()
            streamHandler.setLevel(logging.INFO)

            # 定义Handler的日志输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fileHandler.setFormatter(formatter)

            # 定义日志滚动条件，这里按日期-天保留日志
            timedRotatingFileHandler = handlers.TimedRotatingFileHandler(filename=logFile, when='D')
            timedRotatingFileHandler.setLevel(logging.INFO)
            timedRotatingFileHandler.setFormatter(formatter)

            # 添加Handler
            logger.addHandler(fileHandler)
            logger.addHandler(streamHandler)
            logger.addHandler(timedRotatingFileHandler)

            return logger
        else:
            return cls.logger

Logger.get_logger().info('bbb')