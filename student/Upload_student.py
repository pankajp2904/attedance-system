import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.filedialog as filedialog
import xlrd
import database_proc as dp
from tkinter import messagebox
import temp as table
class student_data:
    Department=["--","CS","CA","IT"]

    Division=["--"]
    list1 = []
    def __init__(self,root):
        self.dataframe=Frame(root)
        self.dataframe2=Frame(root)
        self.dataframe3=Frame(root)
        student_data.upload_student_data(self,root)
    def upload_student_data(self,root):
        self.dataframe3=Frame(root)
        self.dataframe3.grid(row=0,column=0,padx=(0,900),pady=(0,20))
        Dept_lable = tk.Label(self.dataframe3,text=" Select Department")
        Dept_lable.grid(column=0,row=0,padx=(0,50))
        self.Dept_ddl = ttk.Combobox(self.dataframe3,values=student_data.Department)
        self.Dept_ddl.grid(column=0, row=1,padx=(0,10))
        self.Dept_ddl.current(0)
        self.Dept_ddl.bind("<<ComboboxSelected>>", self.Class)
        class_lable = tk.Label(self.dataframe3, text=" Select Class")
        class_lable.grid(column=1, row=0,padx=(0,90))
        self.class_ddl = ttk.Combobox(self.dataframe3)
        self.class_ddl.grid(column=1, row=1,padx=(0,10))
        div_lable = tk.Label(self.dataframe3, text=" Select Division")
        div_lable.grid(column=2, row=0, padx=(0,70))
        div_ddl = ttk.Combobox(self.dataframe3, values=student_data.Division)
        div_ddl.grid(column=2, row=1, padx=(0,10))
        div_ddl.current(0)
        div_lable = tk.Label(self.dataframe3, text=" Inpute file")
        div_lable.grid(column=3, row=0, padx=(0,70))
        self.input_entry =tk.Entry(self.dataframe3, text="", width=40)
        self.input_entry.grid(column=3,row=1,padx=(0,10))
        Upload =tk.Button(self.dataframe3, text="Browse",font=('Arial', 10, 'bold'), command=lambda :student_data.input(self,root,self.Dept_ddl,self.class_ddl,div_ddl))
        Upload.grid(column=4,row=1)

    def input(self,root,Dept_ddl,class_ddl,div_ddl):
        self.list1.clear()
        input_path = tk.filedialog.askopenfilename()
        self.input_entry.delete(1, tk.END)  # Remove current text in entry
        self.input_entry.insert(0, input_path)  # Insert the 'path'
        loc = (input_path)
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        row = sheet.nrows
        for x in range(row):
            values = sheet.row_values(x)
            self.list1.append(values)
        count=0
        for i in self.list1:
            i.insert(0,str(count))
            i.append(Dept_ddl.get())
            i.append(class_ddl.get())
            i.append(div_ddl.get())
            count=count+1
        self.list1[0].remove(Dept_ddl.get())
        self.list1[0].remove(class_ddl.get())
        self.list1[0].remove(div_ddl.get())
        self.list1[0].remove('0')
        self.list1[0].insert(0,"ID")
        self.list1[0].append("Department")
        self.list1[0].append("Class")
        self.list1[0].append("Div")
        total_rows = len(self.list1)
        total_columns = len(self.list1[0])
        self.dataframe.destroy()
        self.dataframe = Frame(root)
        self.dataframe.grid(row=3, column=0)
        table.McListBox(self.dataframe,Col_header=self.list1[0],rows=self.list1[1:],maxmize=500,width=250,checkbox=False)
        self.dataframe2.destroy()
        self.dataframe2 = Frame(root)
        self.dataframe2.grid(row=4,column=0,padx=(0,900))
        Upload_data = tk.Button(self.dataframe2, text="   Upload   ", font=('Arial', 10, 'bold'),
                                command=lambda: student_data.Upload_to_db(self))
        Upload_data.grid(column=0, row=4)
    def Upload_to_db(self):
        self.list1.pop(0)
        for i in self.list1:
           i.pop(0)
        data=dp.insert_student(self.list1)
        if(data!=""):
            messagebox.showinfo("Success", " Student Upload SucessFully")
    def Class(self,event):
        indexs=student_data.Department.index(self.Dept_ddl.get())
        Class = [["--"], ["--","CS I", "CS II"], ["--","MCA I", "MCA II", "MCA III"], ["--","IT I", "IT II"]]
        self.class_ddl["value"]=Class[indexs]
        self.class_ddl.current(0)
