import tkinter as tk
from tkinter import ttk
from tkinter import *
import  temp as table
import database_proc as dp
import FillDroupDown.FillDroupDown as fill
class Assign_subject:
    Department = ["--", "CS", "CA", "IT"]
    Semester = ["--", "SEM 1", "SEM 2", "SEM 3", "SEM 4", "SEM 5", "SEM 6"]
    TeacherList = {}
    SubjectList={}
    def __init__(self,root):
        Assign_subject.displaylist(self,root)
        self.Dept_ddl=None
        self.Teacher_ddl=None
        self.Subject_ddl=None
        self.Sem_ddl=None
        self.tableframe=Frame(root)
        self.droupdown=fill.Droupdown()
        self.Assign_subject=Frame(root)
        Assign_subject.Assign_subject_to_teacher(self,root)
    def Assign_subject_to_teacher(self,root):
        self.Assign_subject = Frame(root)
        self.Assign_subject.grid(row=0,column=0,padx=(0,900),pady=(0,20))
        Dept_lable = tk.Label(self.Assign_subject, text="Select Department")
        Dept_lable.grid(column=0, row=0, padx=(0,50))
        self.Dept_ddl = ttk.Combobox(self.Assign_subject, value=Assign_subject.Department)
        self.Dept_ddl.current(0)
        self.Dept_ddl.grid(column=0, row=1, padx=(0,10))
        self.Dept_ddl.bind("<<ComboboxSelected>>", self.Teacherlist)
        Sem_lable = tk.Label(self.Assign_subject, text="Select Sem")
        Sem_lable.grid(column=1, row=0, padx=(0,90))
        self.Sem_ddl = ttk.Combobox(self.Assign_subject, value=Assign_subject.Semester)
        self.Sem_ddl.grid(column=1, row=1, padx=(0,10))
        self.Sem_ddl.bind("<<ComboboxSelected>>", self.Subjectlist)
        self.Sem_ddl.current(0)
        Teacher_label = tk.Label(self.Assign_subject, text="Select Teacher")
        Teacher_label.grid(column=2, row=0, padx=(0,70))
        self.Teacher_ddl = ttk.Combobox(self.Assign_subject)
        self.Teacher_ddl.grid(column=2, row=1, padx=(0,10))
        Subject_label = tk.Label(self.Assign_subject, text="Assign Subject")
        Subject_label.grid(column=3, row=0, padx=(0,70))
        self.Subject_ddl = ttk.Combobox(self.Assign_subject,width=35)
        self.Subject_ddl.grid(column=3, row=1, padx=(0,10))
        Asign = tk.Button(self.Assign_subject, text="Assign", font=('Arial', 10, 'bold'),command=lambda :Assign_subject.insert_db(self,root))
        Asign.grid(column=4, row=1)
    def insert_db(self,root):
        for key, value in Assign_subject.TeacherList.items():
            if value == self.Teacher_ddl.get():
                teacherid=key
        for key, value in Assign_subject.SubjectList.items():
            if value == self.Subject_ddl.get():
                subjectid=key
        data=[self.Dept_ddl.get(),self.Sem_ddl.get(), teacherid,subjectid]
        print(data)
        id=dp.insert_Assign_Subject(data)
        if(id!=''):
            Assign_subject.displaylist(self,root)
    def displaylist(self,root):
        self.tableframe=Frame(root)
        self.tableframe.grid(row=3,column=0)
        list=dp.get_Assign_Subject()
        header=["ID","Departmenet","Semester","Tecaher","Subject"]
        table.McListBox(root=self.tableframe,Col_header=header,rows=list,maxmize=500,width=100,checkbox=False)
    def Teacherlist(self,event):
        Assign_subject.TeacherList=self.droupdown.fillTeacher(self.Dept_ddl.get())
        self.Teacher_ddl["value"]=list(Assign_subject.TeacherList.values())
        self.Teacher_ddl.current(0)
    def Subjectlist(self,event):
        Assign_subject.SubjectList = self.droupdown.fillSubject(self.Dept_ddl.get(),self.Sem_ddl.get())
        self.Subject_ddl["value"] = list(Assign_subject.SubjectList.values())
        self.Subject_ddl.current(0)

