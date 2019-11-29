from app.log_handler import get_logger
from app.db_handler import MySqlDataBase, System_Sql_Data_Base_Handler

logger = get_logger()

logger.info(msg='tesgdasdfo')

#
# sys_db_handler = System_Sql_Data_Base_Handler()
# sys_db_handler.create_db('giggffe')
# print(*sys_db_handler.get_all_dbs())
# sys_db_handler.del_db('giffe')
#
# print(*sys_db_handler.get_all_dbs())
#


mdb = MySqlDataBase("giraffe")
print(mdb.show_all_tables())

