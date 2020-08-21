'''IMporting'''
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import database_proc as db_proc
import os
import UserRegistartion



class Authentication:
    user = 'admin'
    passw = 'admin'

    def __init__(self, root):

        self.root = root
        self.root.title('USER AUTHENTICATION')

        '''Make Window 10X10'''

        rows = 0
        while rows < 10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows += 1

        '''Username and Password'''

        frame = LabelFrame(self.root, text='Login')
        frame.grid(row=1, column=1, columnspan=10, rowspan=10)

        Label(frame, text=' Usename         ').grid(row=2, column=1, sticky=W,padx=(30, 10),pady=(10,10))
        self.username = Entry(frame)
        self.username.grid(row=2, column=2,padx=(30, 10),pady=(10,10))

        Label(frame, text=' Password ').grid(row=5, column=1, sticky=W,padx=(30, 10),pady=(0,20))
        self.password = Entry(frame, show='*')
        self.password.grid(row=5, column=2,padx=(30, 10),pady=(0,20))

        # Button

        ttk.Button(frame, text='LOGIN', command=self.login_user).grid(row=7, column=1,padx=(80,50),pady=(0,10))
        ttk.Button(frame, text='REGISTER', command=self.Register_user).grid(row=7, column=2,padx=(0,110),pady=(0,10))
        # ttk.Button(frame, text='FaceID(Beta)',command = self.face_unlock).grid(row=8, column=2)

        '''Message Display'''
        self.message = Label(text='', fg='Red')
        self.message.grid(row=10, column=6)

    def login_user(self):
        data=self.username.get()+"|"+self.password.get()
        if(db_proc.login(data)):
            root.destroy()
            os.system(r"Teacher_login.py")
        else:

            '''Prompt user that either id or password is wrong'''
            self.message['text'] = 'Username or Password incorrect. Try again!'

    def Register_user(self):
        root.destroy()
        os.system(r"UserRegistartion\UserRegistration.py")


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    root.geometry('455x200+700+300')
    application = Authentication(root)

    root.mainloop()

