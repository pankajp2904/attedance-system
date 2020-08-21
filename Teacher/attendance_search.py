import tkinter as tk
from tkinter import ttk
from tkinter import *
class Attendance_search:
    Department = ["--", "CS", "CA", "IT"]
    Semester = ["--", "SEM 1", "SEM 2", "SEM 3", "SEM 4", "SEM 5", "SEM 6"]
    TeacherList = {}
    SubjectList = {}
    def __init__(self,root):
        Attendance_search.Attendance_searchs(self,root)
    def Attendance_searchs(self,root):
        Dept_lable=Label(root,text="Select Department")
        Dept_lable.grid(row=0,column=0,padx=(0,50))
        self.dept_ddl=ttk.Combobox(root,value=Attendance_search.Department)
        self.dept_ddl.grid(row=1,column=0,padx=(0,10))
        self.dept_ddl.current(0)
        class_lable = Label(root, text="Select Class")
        class_lable.grid(row=0, column=1,padx=(0,90))
        self.class_ddl = ttk.Combobox(root)
        self.class_ddl.grid(row=1, column=1,padx=(0,10))
        sem_label = Label(root, text="Select Semester")
        sem_label.grid(row=0, column=2,padx=(0,70))
        self.sem_ddl = ttk.Combobox(root)
        self.sem_ddl.grid(row=1, column=2,padx=(0,10))
        Teacher_label = Label(root, text="Select Teacher")
        Teacher_label.grid(row=0, column=3,padx=(0,70))
        self.Teacher_ddl = ttk.Combobox(root)
        self.Teacher_ddl.grid(row=1, column=3, padx=(0, 10))
        Subject_label = tk.Label(root, text="Select Subject")
        Subject_label.grid(column=4, row=0,padx=(0,170))
        self.Subject_ddl = ttk.Combobox(root, width=35)
        self.Subject_ddl.grid(column=4, row=1,padx=(0,10))
        Submit = tk.Button(root, text="Submit", font=('Arial', 10, 'bold'))
        Submit.grid(column=5, row=1)

