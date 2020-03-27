# this is a sample python script program which is used to demonstrate the list box in a widget using the Tkinter library using the Python gui programming.

from Tkinter import *

root=Tk()
list=Listbox(root,width=15)
list.pack()
for item in range(10):
	list.insert(END,item)
	
root.mainloop()

# this is the end of the program file. happy coding..!!