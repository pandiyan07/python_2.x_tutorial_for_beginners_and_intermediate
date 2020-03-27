# this is a sample python script program which is created to demonstrate the concept of adding the sub menus to the original menus.

from Tkinter import *

root=Tk()
menubar=Menu(root)

def hello():
	print"i don't have the slightest idea that what the hell is going on over here."
	
mainmenu=Menu(menubar)

menubar.add_cascade(label='Initial',menu=mainmenu) # the Initial will be the first one on the menu bar

mainmenu.add_command(label="iam number one option",command=hello) # this is the first menu option in the menu icon in the Initial

# creaating the first submenu under the iam number two option under the Initial one.
submenu=Menu(mainmenu)  #  my parent is the hellomenu
submenu.add_command(label="english",command=hello)  # menu item number 1
submenu.add_command(label="spanish",command=hello)  # menu item number 2
submenu.add_command(label="chineese",command=hello) # menu item number 3
submenu.add_command(label="tamil",command=hello)  # menu item number 4

# this is the second option under the icon Initial in the custom menubar
mainmenu.add_cascade(label="iam number two option",menu=submenu)

root.config(menu=menubar)   #  tell the root window to use your menu bar instead of the default one.
root.mainloop()             #  start the event loop.

# this is the end of the program file. happy coding..!!