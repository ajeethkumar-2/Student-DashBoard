import re


class User_Data:

    def login_id(self):
        pattern = '\w'
        while True:
                user_id = input("Enter Your Login ID: ")
                if re.match(pattern, user_id):
                    break
                else:
                    print("Invalid format !!")
        return user_id

    def password(self):
        while True:
            pw = input("Enter Your Password: ")
            pattern = '^.*(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=.{8,}).*$'
            if re.match(pattern, pw):
                break
            else:
                print("Invalid format !!")
                continue
        return pw
    def student_id(self):
        while True:
            s_id = input("Enter the Student ID: ")
            pattern = '^[A-Z]+\d*$'
            if re.match(pattern, s_id):
                break
            else:
                print("Invalid format !!")
                continue
        return s_id

    def name(self):
        while True:
            n = input("Enter the Name: ")
            pattern = '^[A-Z]+?[A-Z | a-z]*\s*?[a-z | A-Z]*\s*?[a-z | A-Z]*$'
            if re.match(pattern, n):
                break
            else:
                print("Invalid format !!")
                continue
        return n

    def dob(self):
        while True:
            birth = input("Enter the Date of Birth(Password): ")
            pattern = '^[\d]+-[\d]+-[\d*]+$'
            if re.match(pattern, birth):
                break
            else:
                print("Invalid format !!")
        return birth

    def department(self):
        while True:
            dep = input("Enter the Department: ")
            pattern = '^[A-Z]+?[a-z|A-Z]+\s*[a-z|A-Z]+$'
            if re.match(pattern, dep):
                break
            else:
                print("Invalid format !!")
                continue
        return dep

    def year(self):
        while True:
            y = input("Enter the Year of Studying: ")
            pattern = '[1-4]'
            if re.match(pattern, y):
                break
            else:
                print("Invalid format !!")
                continue
        return y

    def attendance_percentage(self):
        while True:
            attendance = input("Enter the Overall Attendance Percentage: ")
            pattern = '^[0-9]+[\.]*[0-9]* %$'
            if re.match(pattern,attendance):
                break
            else:
                print("Invalid format !!")
                continue
        return attendance

    def academic_percentage(self):
        while True:
            percentage = input("Enter the Overall Academic Percentage: ")
            pattern = '^[0-9]+[\.*]*[0-9]+ %$'
            if re.match(pattern, percentage):
                break
            else:
                print("Invalid format !!")
                continue
        return percentage

    def records_count(self):
        n = int(input("Enter the count of records to create or modify: "))
        return n

    def enter_choice(self):
        task = {1: 'CREATE AND ADD RECORD', 2:'ADD RECORD',  3: 'UPDATE RECORD', 4: 'DELETE RECORD', 5: 'VIEW ALL RECORDS'}
        print(task)
        choice = int(input("Enter your option: "))
        return choice

    def update_choice(self):
        update = {1: 'NAME', 2: 'DOB', 3: 'DEPARTMENT', 4: 'YEAR', 5: 'ATTENDANCE', 6: 'ACADEMIC', 7: 'PASSWORD'}
        print(update)
        choice = int(input("Enter your key number to update: "))
        return choice

    def login_choice(self):
        option = {1: "ADMIN REGISTRATION", 2: "ADMIN LOGIN", 3: "STUDENT LOGIN"}
        print(option)
        choice = int(input("Enter your option: "))
        return choice

    def admin_reg_choice(self):
        option = {1: "REGISTER FRESH ADMIN", 2: "REGISTER ADDITIONAL ADMIN"}
        print(option)
        choice = int(input("Enter your option: "))
        return choice

#obj = User_Data()

'''obj.login_id()
obj.password()'''
#obj.department()
#obj.dob()
#obj.year()
#obj.student_id()
#obj.attendance_percentage()
#obj.academic_percentage()
#obj.login_choice()