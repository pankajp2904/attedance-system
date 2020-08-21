import tkinter as tk
from tkinter import ttk
from tkinter import *
import  temp as table
import database_proc as dp
import FillDroupDown.FillDroupDown as fill
class Attndance:
    Department = ["--", "CS", "CA", "IT"]
    Semester = ["--", "SEM 1", "SEM 2", "SEM 3", "SEM 4", "SEM 5", "SEM 6"]
    TeacherList = {}
    SubjectList={}
    def __init__(self,root):
        self.Dept_ddl=None
        self.Teacher_ddl=None
        self.Subject_ddl=None
        self.Sem_ddl=None
        self.tableframe=Frame(root)
        self.droupdown=fill.Droupdown()
        self.Attendance=Frame(root)
        Attndance.get_Attendance(self,root)
    def get_Attendance(self,root):
        self.Attendance = Frame(root)
        self.Attendance.grid(column=0,row=0,padx=(0,900),pady=(0,20))
        Dept_lable = tk.Label(self.Attendance, text="Select Department")
        Dept_lable.grid(row=0, column=0,padx=(0,50))
        self.Dept_ddl = ttk.Combobox(self.Attendance, value=Attndance.Department)
        self.Dept_ddl.grid(row=1, column=0, padx=(0, 10))
        self.Dept_ddl.current(0)
        self.Dept_ddl.bind("<<ComboboxSelected>>", self.Teacherlist)
        class_lable = Label(self.Attendance, text="Select Class")
        class_lable.grid(row=0, column=1, padx=(0, 90))
        self.class_ddl = ttk.Combobox(self.Attendance)
        self.class_ddl.grid(row=1, column=1, padx=(0, 10))
        sem_label = Label(self.Attendance, text="Select Semester")
        sem_label.grid(row=0, column=2, padx=(0, 70))
        self.Sem_ddl = ttk.Combobox(self.Attendance,value=Attndance.Semester)
        self.Sem_ddl.grid(row=1, column=2, padx=(0, 10))
        self.Sem_ddl.bind("<<ComboboxSelected>>", self.Subjectlist)
        Teacher_label = Label(self.Attendance, text="Select Teacher")
        Teacher_label.grid(row=0, column=3, padx=(0, 70))
        self.Teacher_ddl = ttk.Combobox(self.Attendance)
        self.Teacher_ddl.grid(row=1, column=3, padx=(0, 10))
        Subject_label = tk.Label(self.Attendance, text="Select Subject")
        Subject_label.grid(column=4, row=0, padx=(0, 170))
        self.Subject_ddl = ttk.Combobox(self.Attendance, width=35)
        self.Subject_ddl.grid(column=4, row=1, padx=(0, 10))
        Submit = tk.Button(self.Attendance, text="Submit", font=('Arial', 10, 'bold'),command=lambda :Attndance.displaylist(self,root))
        Submit.grid(column=5, row=1)
    def insert_db(self):
        P=[]
        P.clear()
        P=self.table_obj.selected_item()
        for key, value in Attndance.TeacherList.items():
            if value == self.Teacher_ddl.get():
                teacherid=key
        for key, value in Attndance.SubjectList.items():
            if value == self.Subject_ddl.get():
                subjectid=key
        data=[self.Dept_ddl.get(),self.class_ddl.get(),self.Sem_ddl.get(), teacherid,subjectid,P]
        print(data)
        id=dp.insert_Attendance(data)
    def displaylist(self,root):
        self.tableframe=Frame(root)
        self.tableframe.grid(column=0,row=3)
        query={"Dept":self.Dept_ddl.get(),"Class":self.class_ddl.get()}
        list=dp.Search(query,3,'Presenti')
        if(list!=[]):
            header=["ID","Roll_No","Name","Presenti"]
            self.table_obj=table.McListBox(root=self.tableframe,Col_header=header,rows=list,maxmize=500,width=300,checkbox=True)
            Submit = tk.Button(self.tableframe, text="Save Attendance", font=('Arial', 10, 'bold'),command=lambda :Attndance.insert_db(self))
            Submit.grid(column=0, row=4,padx=(0,900))
    def Teacherlist(self,event):
        Attndance.TeacherList=self.droupdown.fillTeacher(self.Dept_ddl.get())
        self.Teacher_ddl["value"]=list(Attndance.TeacherList.values())
        self.Teacher_ddl.current(0)
        indexs = Attndance.Department.index(self.Dept_ddl.get())
        Class = [["--"], ["--", "CS I", "CS II"], ["--", "MCA I", "MCA II", "MCA III"], ["--", "IT I", "IT II"]]
        self.class_ddl["value"] = Class[indexs]
        self.class_ddl.current(0)
    def Subjectlist(self,event):
        Attndance.SubjectList = self.droupdown.fillSubject(self.Dept_ddl.get(),self.Sem_ddl.get())
        self.Subject_ddl["value"] = list(Attndance.SubjectList.values())
        self.Subject_ddl.current(0)

