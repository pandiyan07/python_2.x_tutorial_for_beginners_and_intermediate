# this is a sample python script program which is used to demonstrate the entry widget in the python GUI programming

from Tkinter import *

root=Tk()

Label(root,text="Give your input over here :").pack(side=LEFT,padx=5,pady=5)
e=StringVar()
Entry(root,width=60,textvariable=e).pack(side=LEFT,padx=10,pady=10)
e.set("This is a sample input box, which has been created successfully !!")
root.mainloop()

# this is the end of the program file. happy coding..!!