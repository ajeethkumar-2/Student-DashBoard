from validation import *
import pymysql


class StudentsRecord:
    def __init__(self):
        self.ob = User_Data()
        self.db = pymysql.connect("localhost", "root", "", "student_dashboard")
        self.key = self.db.cursor()
        self.key.execute("USE student_dashboard")

    def create_student_table(self):

        try:
            self.key.execute("CREATE TABLE students_record (STUDENT_ID varchar(30) NOT NULL, NAME varchar(30),"
                             "DOB varchar(30), DEPARTMENT varchar(30), YEAR varchar(30), ATTENDANCE varchar(30),"
                             "ACADEMIC varchar(30), PASSWORD varchar(30),  UNIQUE(STUDENT_ID))")
        except Exception as error:
            print(f"Error Occurred: {error}")

    def insert_student_record(self):
        student_id = self.ob.student_id()
        name = self.ob.name()
        dob = self.ob.dob()
        depart = self.ob.department()
        year = self.ob.year()
        attendance = self.ob.attendance_percentage()
        academic = self.ob.academic_percentage()
        #password = self.ob.student_password()  # dob is the password for student
        try:
            self.key.execute("INSERT INTO students_record (STUDENT_ID,NAME,DOB,DEPARTMENT,YEAR,ATTENDANCE,"
                             "ACADEMIC,PASSWORD) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                             % (student_id, name, dob, depart, year, attendance, academic, dob))
            self.db.commit()
        except Exception as error:
            print(f"Error Occurred: {error}")

    def update_student_records(self):
        student_id = self.ob.student_id()
        choice = self.ob.update_choice()
        if choice == 1:
            name = self.ob.name()
            self.key.execute("UPDATE students_record set NAME = '%s' WHERE STUDENT_ID = '%s' " % (name, student_id))
            self.db.commit()
        elif choice == 2:
            dob = self.ob.dob()
            self.key.execute("UPDATE students_record set DOB = '%s' WHERE STUDENT_ID = '%s' " % (dob, student_id))
            self.db.commit()
        elif choice == 3:
            depart = self.ob.department()
            self.key.execute(
                "UPDATE students_record set DEPARTMENT = '%s' WHERE STUDENT_ID = '%s' " % (depart, student_id))
            self.db.commit()
        elif choice == 4:
            year = self.ob.year()
            self.key.execute("UPDATE students_record set YEAR = '%s' WHERE STUDENT_ID = '%s' " % (year, student_id))
            self.db.commit()
        elif choice == 5:
            attendance = self.ob.attendance_percentage()
            self.key.execute(
                "UPDATE students_record set ATTENDANCE = '%s' WHERE STUDENT_ID = '%s' " % (attendance, student_id))
            self.db.commit()
        elif choice == 6:
            academic = self.ob.academic_percentage()
            self.key.execute(
                "UPDATE students_record set ACADEMIC = '%s' WHERE STUDENT_ID = '%s' " % (academic, student_id))
            self.db.commit()
        elif choice == 7:
            pw = self.ob.dob()
            self.key.execute("UPDATE students_record set PASSWORD = '%s' WHERE STUDENT_ID = '%s' " % (pw, student_id))
            self.db.commit()
        else:
            print("Please select valid option")

    def delete_student_record(self):
        student_id = self.ob.student_id()
        self.key.execute("DELETE FROM students_record WHERE STUDENT_ID = '%s' " % student_id)
        self.db.commit()

    def db_close(self):
        self.db.close()
