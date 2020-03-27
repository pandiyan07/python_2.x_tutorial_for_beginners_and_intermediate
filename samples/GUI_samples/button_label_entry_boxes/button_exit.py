# this is a sample python script program which is used to demonstrate the button push exit in the python gui programming.

from Tkinter import *

# hold onto a global reference for the root window.
root=None

def buttonpush():
	global root
	root.destroy()
	
def main():
	global root
	root=Tk() # create the root (base) window  where all widgets go
	
	w=Label(root,text="A very good morning folks..!!\n The button that is below is used to exit the window.")
	w.pack() # put the label into the window
	
	mybutton=Button(root,text="Exit",command=buttonpush)
	mybutton.pack()
	
	root.mainloop() # start the event loop
	
main()
	
# this is the end of the program file. happy coding..!!