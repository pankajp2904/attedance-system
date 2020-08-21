from tkinter import *
import  tkinter as tk
import os
import Student.Upload_student as studsata
import Dashboard as d
import Student.student_search as s
import Setup as setups
import Teacher.Assign_subject as Assign_sub
class Head:
    def __init__(self,root):
        #stud=studsata.student_data()
        self.root = root
        self.bottomframe = Frame(root)
        self.Uploadstudent = Frame(root)
        self.search_student=Frame(root)
        self.setup = Frame(root)
        self.sub_setup=Frame(root)
        self.Subject_Assign=Frame(root)
        self.root.title('Admin Login')
        rows = 0
        while rows < 10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1
    def logout(self):
        root.destroy()
        os.system("login.py")
    def call_Upload_student(self):
        self.bottomframe.destroy()
        self.Uploadstudent.destroy()
        self.search_student.destroy()
        self.setup.destroy()
        self.Uploadstudent = Frame(root)
        self.Uploadstudent.grid(row=0, column=0,padx=(50,0))
        stud = studsata.student_data(self.Uploadstudent)
        #stud.student_data(self.Uploadstudent)
    def call_dashboard(self):
        self.sub_setup.destroy()
        self.Uploadstudent.destroy()
        self.bottomframe.destroy()
        self.setup.destroy()
        self.search_student.destroy()
        self.bottomframe=Frame(root)
        self.bottomframe.grid()
        dashboard=d.Dashboard()
        dashboard.function_call(self.bottomframe)
    def call_search_student(self):
        self.sub_setup.destroy()
        self.Uploadstudent.destroy()
        self.setup.destroy()
        self.bottomframe.destroy()
        self.search_student=Frame(root)
        self.search_student.grid(row=0, column=0,padx=(50,0))
        Search=s.Search_students(self.search_student)
    def call_setup(self):
        self.sub_setup.destroy()
        self.Uploadstudent.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.setup=Frame(root)
        self.setup.grid(row=0,column=0,padx=(50,0))
        obj_setup=setups.setup(self.setup)
    def Call_subject(self):
        self.sub_setup.destroy()
        self.Uploadstudent.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.setup.destroy()
        self.sub_setup = Frame(root)
        self.sub_setup.grid(row=0,column=0,padx=(50,0))
        obj_setup = setups.setup(root)
        obj_setup.subject_setup(self.sub_setup)
    def Call_Assign_Subject(self):
        self.sub_setup.destroy()
        self.Subject_Assign.destroy()
        self.Uploadstudent.destroy()
        self.bottomframe.destroy()
        self.search_student.destroy()
        self.setup.destroy()
        self.Subject_Assign = Frame(root)
        self.Subject_Assign.grid(row=0, column=0,padx=(50,10))
        Assign_sub.Assign_subject(self.Subject_Assign)

if __name__ == '__main__':
    root = Tk()
    root.geometry('900x700')
    application = Head(root)

    application.call_dashboard()
    menubar = Menu(root)
    search = Menu(menubar, tearoff=0)
    setup = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Home",command=lambda :application.call_dashboard())
    menubar.add_cascade(label="Upload Student",command=lambda :application.call_Upload_student())
    menubar.add_cascade(label="Search", menu=search)
    search.add_command(label="Student",command=lambda :application.call_search_student())
    search.add_separator()
    search.add_command(label="Teacher")
    menubar.add_cascade(label="Setup",menu=setup)
    setup.add_command(label="Class Setup" ,command=lambda :application.call_setup())
    setup.add_separator()
    setup.add_command(label="Subject setup",command=lambda :application.Call_subject())
    setup.add_separator()
    setup.add_command(label="Assign Subject", command=lambda: application.Call_Assign_Subject())
    menubar.add_cascade(label="Logout",command=lambda :application.logout())
    root.config(menu=menubar)
    root.mainloop()
