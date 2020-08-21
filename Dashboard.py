import tkinter as tk
from tkinter import *
import database_proc as proc
class Dashboard:
    def Total_Student(self,root):
        count=proc.count({},3)
        frame1 = LabelFrame(root, text='Total No Of Student')
        frame1.grid(row=0, column=2,padx=(50, 10))
        self.Student_count=Label(frame1, text=count).grid(row=2, column=1,padx=(90, 90),pady=(40,40))

    def Total_Teacher(self,root):
        count=proc.count({},2)
        frame = LabelFrame(root, text='Total No Of Teacher')
        frame.grid(row=0, column=4, padx=(50, 10))
        self.Student_count = Label(frame, text=count).grid(row=2, column=1,padx=(90, 90),pady=(40,40))


    def BranchWise_student(self,root):
        frame = LabelFrame(root, text='Branch Wise Student')
        frame.grid(row=0, column=6, padx=(50, 10))
        self.Student_count = Label(frame, text='').grid(row=2, column=1, padx=(90, 90), pady=(40,40))

    def BranchWise_Teacher(self,root):
        frame = LabelFrame(root, text='Branch Wise Teacher')
        frame.grid(row=1, column=2, padx=(50, 10),pady=(30,20))
        self.Student_count = Label(frame, text='').grid(row=2, column=1, padx=(90, 90), pady=(40, 40))

    def function_call(self,root):
        self.Total_Teacher(root)
        self.Total_Student(root)
        self.BranchWise_student(root)
        self.BranchWise_Teacher(root)