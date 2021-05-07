from validation import *
import pymysql
from feedback import *


class AdminRegistration:
    def __init__(self):
        self.obj = User_Data()
        self.fed = Feedback()
        self.db = pymysql.connect("localhost", "root", "", "student_dashboard")
        self.key = self.db.cursor()
        self.key.execute("USE student_dashboard")

    def create_admin_table(self):
        try:
            self.key.execute("CREATE TABLE admin (LOGIN_ID varchar(30), PASSWORD varchar(30), UNIQUE(LOGIN_ID))")
            self.fed.table_feedback()
        except Exception as error:
            print(f"Error Occurred: {error}")

    def create_admin_record(self):
        while True:
            x = self.obj.login_id()
            y = self.obj.password()
            try:
                self.key.execute("INSERT INTO admin (LOGIN_ID,PASSWORD) VALUES('%s', '%s')"
                                 % (x, y))
                self.db.commit()
                self.db.close()
                self.fed.registration_feedback()
            except Exception as error:
                print(f"Error Occurred: {error}")
                continue
            break

    def id_check(self, m, n):
        self.key.execute("select * from admin where LOGIN_ID = '%s' and PASSWORD = '%s' " % (m, n))
        get = self.key.fetchone()
        return get


'''ob = Registration()
ob.create_admin_table()
ob.create_admin_record()'''
