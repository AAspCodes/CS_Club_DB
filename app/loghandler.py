import logging


class LogHandler:
    LOG_FORMAT = "%(levelname)s %(asctime)s %(filename)s  %(funcName)s - %(message)s"
    logging.basicConfig(filename="./debug_logger.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=LOG_FORMAT)
    logger = logging.getLogger()


def get_logger():
    return LogHandler.logger
