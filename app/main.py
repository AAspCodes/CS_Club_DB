from app.loghandler import get_logger

logger = get_logger()

logger.info(msg='tesgdasdfo')

from app.plotter import Plotter
from app.html_formatter import HtmlFormatter


def open_brower_tab():
    import webbrowser
    webbrowser.open_new("file:///Users/pro/Documents/ProgrammingFiles/Python/PycharmProjects/CS_Club_DB/index.html")


data1 = ([1, 2, 34, 4], [1, 20, 5, 21])
data2 = ([1, 2, 5, 4], [1, 7, 5, 2])


html = Plotter(data1).plot_html()
HtmlFormatter(html, "index.html").main()

html = Plotter(data2).plot_html()
HtmlFormatter(html, "index1.html").main()

open_brower_tab()

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
