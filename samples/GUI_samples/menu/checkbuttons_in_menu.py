# this is a sample python script program which is used to demonstrate the concept of including checkbuttons in the options in the menu bar in the python GUI programming.

from Tkinter import *

root=Tk()
mbr=Menu(root)
chkbtn=Menu(mbr)
root.title("check buttons in the menu options")

mbr.insert_cascade(index=0,label='Checkbutton Menus',underline=0,menu=chkbtn)	

chkbtn.add_checkbutton(label='apple')
chkbtn.add_checkbutton(label='mango')
chkbtn.add_checkbutton(label='grapes')
chkbtn.add_checkbutton(label='orange')
chkbtn.add_checkbutton(label='gauva')
	
chkbtn.invoke(chkbtn.index('mango'))		#  this invoke function is for keeping the mango function as a selected option by default.

root.config(menu=mbr)	
root.mainloop()

# this is the end of the program file. happy coding..!!