# this is a sample python script program which is used to demonstrate the radio button in the menu's options list in the python GUI programming.

from Tkinter import *

root=Tk()
mbr=Menu(root)
radbtn=Menu(mbr)
root.title("radio buttons in the menu options")

mbr.insert_cascade(index=0,label='Radiobutton menus',underline=0,menu=radbtn)
	
radbtn.add_radiobutton(label='apple')
radbtn.add_radiobutton(label='mango')
radbtn.add_radiobutton(label='banana')
radbtn.add_radiobutton(label='grapes')
radbtn.add_radiobutton(label='orange')

radbtn.invoke(radbtn.index('grapes'))  #  we invoke the function for keeping the gapes option in the main menu bar to be selected by default

root.config(menu=mbr)
root.mainloop()

# this is the end of the program file. happy coding..!!