from tkinter import *
import  tkinter as tk
import os
import Student.Upload_student as studsata
import Dashboard as d
import Student.student_search as s
import Setup as setups
import Teacher.Attendance as Attendance
import Teacher.attendance_search as As
class Teacher_login:
    def __init__(self,root):
        self.root = root
        self.bottomframe = Frame(root)
        self.Uploadstudent = Frame(root)
        self.search_student=Frame(root)
        self.setup = Frame(root)
        self.sub_setup=Frame(root)
        self.Attendanc=Frame(root)
        self.Attendance_search=Frame(root)
        self.root.title('Teacher Login')
        rows = 0
        while rows < 10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1
    def logout(self):
        root.destroy()
        os.system("login.py")
    def call_dashboard(self):
        self.Attendance_search.destroy()
        self.Attendanc.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.bottomframe=Frame(root)
        self.bottomframe.grid()
        dashboard=d.Dashboard()
        dashboard.function_call(self.bottomframe)
    def call_search_student(self):
        self.Attendance_search.destroy()
        self.Attendanc.destroy()
        self.search_student.destroy()
        self.bottomframe.destroy()
        self.search_student=Frame(root)
        self.search_student.grid(row=0, column=0,padx=(50,0))
        Search=s.Search_students(self.search_student)
    def Call_subject(self):
        self.Attendance_search.destroy()
        self.Attendanc.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.setup.destroy()
        self.sub_setup = Frame(root)
        self.sub_setup.grid(row=0,column=1)
        obj_setup = setups.setup(root)
        obj_setup.subject_setup(self.sub_setup)
    def Call_Attendance(self):
        self.Attendance_search.destroy()
        self.Attendanc.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.setup.destroy()
        self.Attendanc = Frame(root)
        self.Attendanc.grid(row=0, column=0,padx=(50,0))
        Attendance.Attndance(self.Attendanc)
    def call_Attendance_search(self):
        self.Attendance_search.destroy()
        self.Attendanc.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.Attendance_search=Frame(root)
        self.Attendance_search.grid(row=0,column=0,padx=(50,0))
        As.Attendance_search(self.Attendance_search)


if __name__ == '__main__':
    root = Tk()
    root.geometry('1100x700')
    application = Teacher_login(root)

    application.call_dashboard()
    menubar = Menu(root)
    setup = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Home",command=lambda :application.call_dashboard())
    menubar.add_cascade(label="Student Search",command=lambda :application.call_search_student())
    menubar.add_cascade(label="Attendance",command=lambda :application.Call_Attendance())
    menubar.add_cascade(label="Search Attendance", command=lambda: application.call_Attendance_search())
    menubar.add_cascade(label="Logout",command=lambda :application.logout())
    root.config(menu=menubar)
    root.mainloop()
