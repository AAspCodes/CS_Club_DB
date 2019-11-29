from app.log_handler import get_logger
from app.db_handler import MySqlDataBase

logger = get_logger()

logger.info(msg='hello')


mydb = MySqlDataBase()
