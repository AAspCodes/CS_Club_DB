import logging
logging.basicConfig(filename="/Users/pro/Documents/ProgrammingFiles/Python/PycharmProjects/CS_Club_DB/app/debug_logger.log",
                    level=logging.DEBUG,
                    filemode="w")
logger = logging.getLogger()

logger.info("testing123")

