
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import *
from datetime import date
class McListBox:
    increment=0
    def __init__(self,root,Col_header,rows,maxmize,width,checkbox):
        self.m = Menu(root, tearoff=0)
        self.m.add_command(label="Delete")
        self.m.add_command(label="Edit")
        self.tree = None
        self.header=Col_header
        self.row=rows
        self.checkbox=checkbox
        self.vars = []
        self.maxmize=maxmize
        self.width=width
        self.buttons=None
        self.container = ttk.Frame(root)
        McListBox._setup_widgets(self,root)
        McListBox._build_tree(self)
    def _setup_widgets(self,root):
        self.container.destroy()
        self.container = ttk.Frame(root)
        self.container.grid(row=1,column=0,padx=(0,900))
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=self.header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.container)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.container)
        hsb.grid(column=0, row=1, sticky='ew', in_=self.container)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1,minsize=self.maxmize)
    def _build_tree(self):
        McListBox.increment = 0
        for col in self.header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: McListBox.sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        for item in self.row:
            list=[]
            self.var = StringVar()
            list.append(item[0])
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(self.header[ix],width=None)<col_w:
                    self.tree.column(self.header[ix], width=col_w+int(self.width))
            if(self.checkbox==True):
                chk=ttk.Checkbutton(self.tree,onvalue=item[0],variable=self.var).place(x=500, y=25+McListBox.increment)
                McListBox.increment=McListBox.increment+20
                self.vars.append(self.var)
            self.tree.column('ID',width=50)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
    def sortby(tree, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
        # if the data to be sorted is numeric change to float
        #data =  change_numeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        tree.heading(col, command=lambda col=col: McListBox.sortby(tree, col, \
            int(not descending)))
    def do_popup(self,event):
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()
    def on_tree_select(self,event):
            curItem = self.tree.focus()
            self.tree.bind("<Button-3>", self.do_popup)
            a=self.tree.item(curItem,"values")
            print(a[0])
            return a[0]
    def selected_item(self):
        list1=[]
        for c in self.vars:
            if(c.get()!=''):
              list1.append(int(c.get()))
        print(list)
        return list1