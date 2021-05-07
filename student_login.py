from admin_login import *
from student_record_entry import *
from validation import *
from admin_login import *


class StudentLogin:
    def __init__(self):
        #self.obj = Registration()
        self.ob = User_Data()
        self.fed = Feedback()
        self.admin = AdminLogIn()
        self.db = pymysql.connect("localhost", "root", "", "student_dashboard")
        self.key = self.db.cursor()
        self.key.execute("USE student_dashboard")


    def student_login(self):
        while True:
            s_id = self.ob.student_id()
            pw = self.ob.dob()
            get = self.admin.fetch_student_login(s_id, pw)
            #print(get)
            if get is not None:
                if s_id == get[0] and pw == get[-1]:
                    self.fed.login_feedback()
                    self.admin.print_one_record(s_id)

            else:
                print("PLease Check Student ID and Password you entered !!")
                continue
            break

#obj = StudentLogin()
#obj.student_login()