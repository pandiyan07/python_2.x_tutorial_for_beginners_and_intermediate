# this is a sample python script program which is used to use the scroll bar in the widget or window with the help of Tkinter library in the python gui programming

from Tkinter import *

root=Tk()

list=Listbox(root,height=6,width=15)
scroll=Scrollbar(root,command=list.yview)
list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)
for item in range(30):
	list.insert(END,item)

root.mainloop()

# this is the end of the program file. happy coding..!!