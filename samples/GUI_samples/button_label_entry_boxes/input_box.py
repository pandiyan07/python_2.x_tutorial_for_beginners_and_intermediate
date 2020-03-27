# this is a sample python script program which is used to demonstrate the creation of text box in the window and take a input in python
# gui programming.

from Tkinter import *

# hold onto a global reference for the root window 
root=None

# Hold onto the text entry box also
entrybox=None

def buttonpushed():
	global entrybox
	txt=entrybox.get()
	print'The text you have entered is:\n>\t', txt
	
def createtextbox(pandiyan):
	global entrybox
	entrybox=Entry(pandiyan)
	entrybox.pack()  # put the entry box into the window
	
def main():
	global root
	root=Tk() # create a root window or a base window where all widgets go
	
	createtextbox(root)
	
	mybutton=Button(root,text="Show me the input",command=buttonpushed)
	mybutton.pack()  # put the mubutton object into the window
	
	root.mainloop() # starting the event loop
	
main()

# this is the end of the program file . happy coding..!!