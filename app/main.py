from app.log_handler import get_logger
from app.db_handler import MySqlDataBase, System_Sql_Data_Base_Handler

logger = get_logger()

logger.info(msg='tesgdasdfo')

from app.plotter import Plotter
from app.html_formatter import HtmlFormatter




data = ([1,2,34,4], [1,20, 5, 21])

html = Plotter(data).plot_html()
HtmlFormatter(html).main()





#
# sys_db_handler = System_Sql_Data_Base_Handler()
# sys_db_handler.create_db('giggffe')
# print(*sys_db_handler.get_all_dbs())
# sys_db_handler.del_db('giffe')
#
# print(*sys_db_handler.get_all_dbs())
#

#
# mdb = MySqlDataBase("giraffe")
# print(mdb.show_all_tables())

