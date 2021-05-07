from validation import *
from admin_registration import *
from student_record_entry import *
from feedback import *
from tabulate import *


class AdminLogIn:
    def __init__(self):
        self.obj = AdminRegistration()
        self.ob = User_Data()
        self.fed = Feedback()
        self.ent = StudentsRecord()
        self.db = pymysql.connect("localhost", "root", "", "student_dashboard")
        self.key = self.db.cursor()
        self.key.execute("USE student_dashboard")

    def admin_login(self):
        while True:
            user = self.ob.login_id()
            pw1 = self.ob.password()
            # pw2 = self.ob.password()
            get = self.obj.id_check(user, pw1)
            if get is not None:
                if user == get[0] and pw1 == get[1]:
                    self.fed.login_feedback()
                    choice = self.ob.enter_choice()
                    if choice == 1:
                        self.ent.create_student_table()
                        self.fed.table_feedback()
                        self.ent.insert_student_record()
                        self.fed.record_feedback()
                        self.ent.db_close()
                    elif choice == 2:
                        count = self.ob.records_count()
                        s = 0
                        while s < count:
                            self.ent.insert_student_record()
                            self.fed.record_feedback()
                            s += 1
                        self.ent.db_close()
                    elif choice == 3:
                        count = self.ob.records_count()
                        s = 0
                        while s < count:
                            self.ent.update_student_records()
                            self.fed.update_feedback()
                            s += 1
                        self.ent.db_close()

                    elif choice == 4:
                        count = self.ob.records_count()
                        s = 0
                        while s < count:
                            self.ent.delete_student_record()
                            self.fed.delete_feedback()
                            s += 1
                        self.ent.db_close()

                    elif choice == 5:
                        self.print_all_records()
            else:
                print("Please check your Login Id and Password !!")
                continue
            break

    def fetch_all_data(self):
        self.key.execute("select * from students_record")
        get = [i for i in self.key.fetchall()]
        return get

    def fetch_student_login(self, m, n):
        self.key.execute("select * from students_record where STUDENT_ID = '%s' and PASSWORD = '%s' " % (m, n))
        get = self.key.fetchone()
        return get

    def fetch_student_data(self, m):
        self.key.execute("select * from students_record where STUDENT_ID = '%s'" % m)
        d = self.key.fetchone()
        return d

    def print_one_record(self, m):
        d = self.fetch_student_data(m)
        data = [[d[0], d[1], d[-3], d[-2]]]
        #print(data)
        headers = ["STUDENT ID", "NAME", "ATTENDANCE PERCENTAGE", "ACADEMIC PERCENTAGE"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def print_all_records(self, ):
        data = self.fetch_all_data()
        headers = ["STUDENT ID", "NAME", "DOB", "DEPARTMENT", "YEAR", "ATTENDANCE PERCENTAGE", "ACADEMIC PERCENTAGE", "PASSWORD"]
        print(tabulate(data, headers=headers, tablefmt="grid", colalign="center", showindex="always"))




#z = AdminLogIn()
#z.signin(
#z.fetch_all_data()
#z.print_table()