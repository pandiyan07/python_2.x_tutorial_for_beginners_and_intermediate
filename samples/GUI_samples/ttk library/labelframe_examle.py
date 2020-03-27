# this is a sample python program  which is used to demonstrate the use of LabelFrame using the ttk library

from Tkinter import  *
import ttk
root=Tk()
root.config(bg='black')
ld=ttk.LabelFrame(root,text="hello",width=200, height=100)
ld.pack(padx=5,pady=5)
root.mainloop()

# this is the end of the python program. happy coding...!!