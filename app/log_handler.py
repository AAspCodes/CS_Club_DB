import logging


class Log_Handler:

    LOG_FORMAT = "%(levelname)s %(asctime)s %(filename)s  %(funcName)s - %(message)s"
    logging.basicConfig(filename="/Users/pro/Documents/ProgrammingFiles/Python/PycharmProjects/CS_Club_DB/app/debug_logger.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=LOG_FORMAT)
    logger = logging.getLogger()


def get_logger():
    return Log_Handler.logger
