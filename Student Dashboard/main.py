from validation import *
from admin_registration import *
from admin_login import *
from student_login import *


class Main:
    def __init__(self):
        self.obj = User_Data()
        self.ob = StudentLogin()
        self.reg = AdminRegistration()
        self.adm = AdminLogIn()

    def main(self):
        choice = self.obj.login_choice()
        if choice == 1:
            reg_choice = self.obj.admin_reg_choice()
            if reg_choice == 1:
                self.reg.create_admin_table()
                self.reg.create_admin_record()
            elif reg_choice == 2:
                self.reg.create_admin_record()
            else:
                print("Please enter valid input")

        elif choice == 2:
            self.adm.admin_login()

        elif choice == 3:
            self.ob.student_login()


if __name__ == '__main__':
    op = Main()
    op.main()

