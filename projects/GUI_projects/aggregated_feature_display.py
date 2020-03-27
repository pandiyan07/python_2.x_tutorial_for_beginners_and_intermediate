# this is a python script program which is consists of all the features combined together and displayed in the same window.

from Tkinter import *

root=Tk()

# this is the Menu section designing part.
		
def printer():
	print ' hey there !!.. you have clicked some button.'
	
menubar=Menu(root)
subma=Menu(menubar)
submb=Menu(menubar)
#submenuu=Menu(mainmenu)

menubar.add_cascade(label="File",menu=subma)     # this is the first menu item in the menu bar that is the file menu item

subma.add_command(label="New",command=printer)          # the first menu item under the File menu
subma.add_command(label="Open",command=printer)         # the second item under the file menu
subma.add_command(label="Save",command=printer)          # the third item under the  file menu
subma.add_command(label="Save as",command=printer)       # the fourth item under the file menu
subma.add_command(label="Close",command=printer)         # this is the fifth item under the file menu
subma.add_command(label="Close all",command=printer)    # this is the sixth item under the file menu

menubar.add_cascade(label="Edit",menu=submb)     # this is the second menu item in the menu bar that is Edit menu item

submb.add_command(label="Undo",command=printer)          # this is the first menu item under the Edit menu
submb.add_command(label="Redo",command=printer)          # this is the second menu item under the Edit menu
submb.add_command(label="Copy",command=printer)          # this is the third menu item under the Edit menu
submb.add_command(label="Paste",command=printer)         # this is the fourth menu item under the Edit menu
submb.add_command(label="Delete",command=printer)        # this is the fifth menu item under the Edit menu
submb.add_command(label="Select all",command=printer)    # this is the sixth menu item under the Edit menu
		
root.config(menu=menubar)     # this statement is to provide that to take this custom made menubar instead of the default menubar

# this is the interior designing part that is within the window under the Menu section.

texta="""This is a sample python GUI application which has been created only for practice purpose only.
The below statement is a sample ,message box"""

textb=""" This is a sample text box and you are viewing a good example of it.This sample message box is a part of this window that you are viewing and 
i would like to appreciate me or applaude me for this work of mine."""

firstframe=Frame(root,width=550,height=70)

secondframe=Frame(firstframe,relief=SOLID,borderwidth=5)
secondframe.place(relx=0.01,rely=0.01,anchor=NW)
Label(firstframe,text="Good morning folks").place(relx=0.05,rely=0.015,anchor=W)

Label(secondframe,text=texta).pack(pady=10,padx=10)

firstframe.pack(padx=0,pady=10)	

# this is a sample message window which will be included below the above the first frame.

root.title("Message box")
Message(root,text=textb,bg='black',fg='white',relief=GROOVE).pack(padx=10,pady=10)

root.mainloop()       # this is statement is provided to start the event loop

#   this is the end of the program file. happy coding..!!