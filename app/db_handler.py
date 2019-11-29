import mysql.connector as msc
from app.log_handler import get_logger

class SqlSuperHandler:


    def sql_command(self, entry_command):
        """execute an SQL command"""
        self.myc.execute(entry_command)

class System_Sql_Data_Base_Handler(SqlSuperHandler):


    def __init__(self):
        self.logger = get_logger()
        self.db = self.connect_to_db()
        self.myc = self.db.cursor()

    def connect_to_db(self):
        mydb = msc.connect(host='localhost', user='root', passwd='password', auth_plugin='mysql_native_password')
        self.logger.info(msg="Connect to Database")
        return mydb


    def create_db(self, name):
        try:
            self.sql_command('CREATE DATABASE {0}'.format(name))
        except msc.errors.DatabaseError as e:
            print(f"The {name} data base already exists")
            self.logger.error(e)
        else:
            msg = "data base {0} was created".format(name)
            print(msg)
            self.logger.info(msg=msg)


    def get_all_dbs(self):
        self.sql_command('SHOW DATABASES')
        return self.myc

    def show_all_dbs(self):
        self.sql_command('SHOW DATABASES')
        for i in self.myc:
            print(i)

    def del_db(self, name):
        self.sql_command("DROP DATABASE {0}".format(name))


class MySqlDataBase(SqlSuperHandler):

    def __init__(self, name):
        self.logger = get_logger()
        self.name = name
        self.db = self.connect_to_db(name)
        self.myc = self.db.cursor()

    def connect_to_db(self, name):
        mydb = msc.connect(host='localhost',
                           user='root',
                           passwd='password',
                           auth_plugin='mysql_native_password',
                           database=name)
        self.logger.info(msg="Connect to Database: {0}".format(name))
        return mydb


    def create_table(self, name, primary_key, pk_data_type):
        # try:
        self.myc.execute(f'CREATE Table {name} ({primary_key} {pk_data_type});')
        # except msc.errors.DatabaseError as e:
        #     print(f"The {name} data base already exists")
        #     self.logger.error(e)
        # else:
        #     msg = "data base {0} was created".format(name)
        #     print(msg)
        #     self.logger.info(msg=msg)


    def del_table(self, name):
        self.sql_command("DROP {0}".format(name))


    def show_all_tables(self):
        self.sql_command("SHOW TABLES ")
        print(*self.myc)

    def show_table(self,name):
        self.sql_command("SHOW TABLES ")

