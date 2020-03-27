# this is a sample python script program which is used to demonstrate the concept of creating a changable label in the window
# using the python gui programming

# use  a stringvar to create a changable label name

from Tkinter import *

# hold onto a global reference for the root window
root=None

# changable text that will go inside the label
mytext=None
count=0 
# click counter

def buttonpushed():
	global mytext
	global count
	count+=1
	mytext.set("stop your clicking ,it's already been %d times"%(count))
	
def addtextlabel(root):
	global mytext
	mytext=StringVar()
	mytext.set("")

	mylabel=Label(root,textvariable=mytext)
	mylabel.pack()
	
def main():
	global root
	root=Tk() # create the root window or the base window where all the widgets go
	
	w=Label(root,text="click the below given button")
	w.pack()
	mybutton=Button(root,text="Show text",command=buttonpushed)
	mybutton.pack()
	
	addtextlabel(root)
	root.mainloop()  # start the main loop
	
main()

# this is the end of the program file . happy coding..!!