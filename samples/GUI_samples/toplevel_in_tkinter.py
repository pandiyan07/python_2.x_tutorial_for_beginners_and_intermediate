# this is a sample python program which uses tkinter to demonstrate top level widget 

from Tkinter import *

root = Tk()
root.geometry('600x200')
L1=Label(root,text="this is the ROOT widget",bg="blue",fg="white")
L1.pack()

top = Toplevel()
top.geometry('400x400')
L2=Label(top,text="this is the TOPLEVEL widget",bg="darkgreen",fg="white")
L2.pack()

top.mainloop()

# this is the end of the python program. happy coding...!!