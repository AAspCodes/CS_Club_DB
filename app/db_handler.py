import mysql.connector as msc




class My_Db:

    def __init__(self):
        self.db = self.connect_to_db()
        self.myc = self.db.cursor()


    def connect_to_db(self):
        mydb = msc.connect(host='localhost', user='root', passwd='password', auth_plugin='mysql_native_password')
        return mydb


    def create_db(self, name):
        self.myc.execute('CREATE DATABASE {0}'.format(name))

    def get_all_dbs(self):
        self.myc.execute('SHOW DATABASES')
        return self.myc


    def show_all_dbs(self):
        self.myc.execute('SHOW DATABASES')
        for i in self.myc:
            print(i)






mydb = My_Db()



mydb.show_all_dbs()
mydb.show_all_dbs()
mydb.show_all_dbs()