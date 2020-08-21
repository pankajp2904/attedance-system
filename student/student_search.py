import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.filedialog as filedialog
import xlrd
import temp as t
import database_proc as dp
from tkinter import messagebox
class Search_students:
    Department=["--","CS","CA","IT"]
    Class=["--"]
    Division=["--"]
    list1 = []
    def __init__(self,root):
        self.dataframe=Frame(root)
        self.dataframe2=Frame(root)
        Search_students.Search_student(self,root)
    def Search_student(self,root):
        self.src = Frame(root)
        self.src.grid(row=0,column=0,padx=(0,900),pady=(0,20))
        Dept_lable = tk.Label(self.src,text=" Select Department")
        Dept_lable.grid(column=0,row=0,padx=(0,50))
        Dept_ddl = ttk.Combobox(self.src,values=Search_students.Department)
        Dept_ddl.grid(column=0, row=1,padx=(0,10))
        Dept_ddl.current(0)
        class_lable = tk.Label(self.src, text=" Select Class")
        class_lable.grid(column=1, row=0,padx=(0,90))
        class_ddl = ttk.Combobox(self.src, values=Search_students.Class)
        class_ddl.grid(column=1, row=1,padx=(0,10))
        class_ddl.current(0)
        div_lable = tk.Label(self.src, text=" Select Division")
        div_lable.grid(column=2, row=0, padx=(0,70))
        div_ddl = ttk.Combobox(self.src, values=Search_students.Division)
        div_ddl.grid(column=2, row=1, padx=(0, 10))
        div_ddl.current(0)
        div_lable = tk.Label(self.src, text="Roll No")
        div_lable.grid(column=3, row=0, padx=(0,70))
        Roll_no=tk.Entry(self.src,width=20)
        Roll_no.grid(column=3, row=1,padx=(0,10))
        Search =tk.Button(self.src, text="Search",font=('Arial', 10, 'bold'),command=lambda :Search_students.stude_search(self,Dept_ddl,class_ddl,div_ddl,Roll_no,root))
        Search.grid(column=4,row=1)
    def Display_table(self,total_columns,total_rows,root):
        # code for creating ta
        self.dataframe.destroy()
        self.dataframe = Frame(root)
        self.dataframe.grid(row=1, column=0,padx=(50,470))
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = tk.Entry(self.dataframe, width=20, font=('Arial', 10, 'bold'))
                self.e.grid(row=i, column=j,sticky=W)
                self.e.insert(END, self.list1[i][j])
                self.e.config(state='disabled')
        self.dataframe2.destroy()
        self.dataframe2 = Frame(root)
        self.dataframe2.grid(row=total_rows+2, column=0)
        Next = tk.Button(self.dataframe2, text=" >>> ", font=('Arial', 10, 'bold'))
        Next.grid(column=total_columns + 1, row=total_rows + 1, pady=(10, 10), padx=(400, 300))
        Prev = tk.Button(self.dataframe2, text="  <<<  ",font=('Arial', 10, 'bold'))
        Prev.grid(column=total_columns+1, row=total_rows+1,pady=(10,10),padx=(300,300))
    def stude_search(self,Dept_ddl,class_ddl,div_ddl,Roll_no,root):
        dict={}
        self.list1.clear()
        if(Dept_ddl.get()!="--"):
            dict.update({"Dept":Dept_ddl.get()})
        if(class_ddl.get()!="--"):
            dict.update({"Class": class_ddl.get()})
        if(div_ddl.get()!="--"):
            dict.update({"Div": div_ddl.get()})
        if(len(Roll_no.get())!=0):
            dict.update({"Roll_no": int(Roll_no.get())})
        self.list1=dp.Search(dict,3,'')
        if(self.list1!=[]):
            self.list1.insert(0, ["ID","Roll NO","Name", "Department", "Class"])
            total_rows =len(self.list1)
            total_columns = len(self.list1[0])
            #Search_students.Display_table(self,total_columns,total_rows,root)
            self.dataframe.destroy()
            self.dataframe = Frame(root)
            self.dataframe.grid(row=3, column=0)
            object=t.McListBox(self.dataframe,self.list1[0],self.list1[1:],maxmize=500,width=250,checkbox=False)

        else:
            self.dataframe.destroy()
            self.dataframe2.destroy()
