import tkinter as tk
from  tkinter import  ttk
from tkinter import *
import database_proc
import temp as t
class setup:
    Department = ["--", "CS", "CA", "IT"]
    Semester=["--","SEM 1","SEM 2","SEM 3","SEM 4","SEM 5","SEM 6"]
    def __init__(self,root):
        self.Dept=Frame(root)
        self.Class=Frame(root)
        self.Div=Frame(root)
        self.Sub=Frame(root)
        self.tableFrame=Frame(root)
        #setup.Dept_setup(self,root)
        #setup.Class_setup(self,root)
    def Dept_setup(self,root):
        self.Dept=Frame(root)
        self.Dept.grid(row=0,column=0,padx=(20,900),pady=(0,500))
        Dept_lable = tk.Label(self.Dept, text="Department Name")
        Dept_lable.grid(column=0, row=0, padx=(0, 900))
        Dept_text=tk.Entry(self.Dept,width=20, font=('Arial', 10, 'bold'))
        Dept_text.grid(column=0,row=1,padx=(35,900))
        submit_dept = tk.Button(self.Dept, text="Submit", font=('Arial', 10, 'bold'))
        submit_dept.grid(column=0, row=1,padx=(60,700))
    def Class_setup(self,root):
        self.Class=Frame(root)
        self.Class.grid(row=0,column=0,padx=(0,900))
        Dept_lable = tk.Label(self.Class, text="Select Department")
        Dept_lable.grid(column=0, row=0,padx=(0,900))
        Dept_ddl = ttk.Combobox(self.Class)
        Dept_ddl.grid(column=0, row=0, padx=(45, 900), pady=(50, 10))
        Class_lable = tk.Label(self.Class, text="Class Name")
        Class_lable.grid(column=0, row=0, padx=(100, 700))
        Dept_text = tk.Entry(self.Class, width=20, font=('Arial', 10, 'bold'))
        Dept_text.grid(column=0, row=0, padx=(185, 700), pady=(50, 10))
        submit_class = tk.Button(self.Class, text="Submit", font=('Arial', 10, 'bold'))
        submit_class.grid(column=0, row=0, padx=(120, 400), pady=(50, 10))
    def subject_setup(self,root):
        self.Dept.destroy()
        self.Class.destroy()
        self.Sub=Frame(root)
        self.Sub.grid(row=0,column=0,padx=(0,900),pady=(0,20))
        setup.Subject_list(self,root)
        Dept_lable = tk.Label(self.Sub, text="Select Department")
        Dept_lable.grid(column=0, row=0, padx=(0,50))
        Dept_ddl = ttk.Combobox(self.Sub,value=setup.Department)
        Dept_ddl.current(0)
        Dept_ddl.grid(column=0, row=1, padx=(0,10))
        Sem_lable = tk.Label(self.Sub, text="Select Sem")
        Sem_lable.grid(column=1, row=0, padx=(0,90))
        Sem_ddl = ttk.Combobox(self.Sub,value=setup.Semester)
        Sem_ddl.current(0)
        Sem_ddl.grid(column=1, row=1, padx=(0,10))
        Sub_lable = tk.Label(self.Sub, text="Subject Name")
        Sub_lable.grid(column=2, row=0, padx=(0,70))
        Sub_text = tk.Entry(self.Sub, width=40, font=('Arial', 10, 'bold'))
        Sub_text.grid(column=2, row=1, padx=(0,10))
        submit_class = tk.Button(self.Sub, text="Submit", font=('Arial', 10, 'bold'),command=lambda :setup.Submit_subject(self,Dept_ddl,Sem_ddl,Sub_text,self.Sub))
        submit_class.grid(column=3, row=1)
    def Submit_subject(self,Dept_ddl,Sem_ddl,Sub_text,root):
        list=[Dept_ddl.get(),Sem_ddl.get(),Sub_text.get()]
        result=database_proc.inset_Sunject(list)
        if(result!=""):
            print(result)
        setup.Subject_list(self,root)
    def Subject_list(self,root):
        list1=database_proc.get_Subjct(4,{})
        if(list1!=[]):
            total_rows = len(list1)
            total_columns = len(list1[0])
            #self.tableFrame.destroy()
            self.tableFrame = Frame(root)
            self.tableFrame.grid(row=4, column=0)
            object=t.McListBox(self.tableFrame,Col_header=["ID","Department","Semester","Subject"],rows=list1,maxmize=500,width=200,checkbox=False)
    '''def Display_table(self,list1, total_columns, total_rows,root):
        # code for creating table
        self.tableFrame.destroy()
        self.tableFrame = Frame(root)
        self.tableFrame.grid(row=4, column=0, padx=(80,800))
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = tk.Label(self.tableFrame,text=list1[i][j]+"\n",font=('Arial', 10, 'bold'))
                self.e.grid(row=i, column=j, sticky=W)'''