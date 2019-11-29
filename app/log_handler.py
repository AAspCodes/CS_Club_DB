import logging

class log_handler:

    logging.basicConfig(filename="/Users/pro/Documents/ProgrammingFiles/Python/PycharmProjects/CS_Club_DB/app/debug_logger.log",
                    level=logging.DEBUG,
                    filemode="w")
    logger = logging.getLogger()

    @staticmethod
    def log(message):
        log_handler.logger.info(message)
