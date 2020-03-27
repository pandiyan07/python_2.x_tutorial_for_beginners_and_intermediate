# this is a sample python script program which is used to demonstrate the concept of placing the buttons side by side.

from Tkinter import *

# hold on to a global reference to the root window.
root=None
firstcount=0  #first click counter
secondcount=5 # second click counter

def addbutton(root,sidetopack):
	global firstcount
	
	firstcount+=1
	name="Button "+str(firstcount)+" "+sidetopack
	
	button=Button(root,text=name)
	button.pack(side=sidetopack)
	
def anotherbutton(root,sidetopack):
	global secondcount

	secondcount+=1
	name="Button "+str(secondcount)+" "+sidetopack
	
	button=Button(root,text=name)
	button.pack(side=sidetopack)
	
def main():
	global root
	
	root=Tk()  # create the root window or the base window where all the widgets go
	
	frame1=Frame(root)
	for i in range(5):
		addbutton(frame1,TOP)
	frame1.pack(side=LEFT)
	
	frame2=Frame(root)
	for j in range(3):
		anotherbutton(frame2,TOP)
	frame2.pack(side=RIGHT)
		
	root.mainloop()  #start the event loop

main()

# this is the end of the program file . happy coding..!!