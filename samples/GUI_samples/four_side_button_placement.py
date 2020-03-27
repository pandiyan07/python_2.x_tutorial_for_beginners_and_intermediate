# this is a sample python script program which is used demonstrate the concept of placing the buttons in the all sides.

from Tkinter import *

# hold onto a global reference for the root window
root=None
count=0 # click the counter

def addbutton(root,sidetopack):
	global count
	count+=1
	
	name="button "+str(count)+" "+sidetopack
	
	button=Button(root,text=name)
	button.pack(side=sidetopack)
	
def main():
	global root
	root=Tk()  # create the root window or the base window where all the widgets go
	
	addbutton(root,LEFT)  #  put the left side of the next widget close to me
	addbutton(root,BOTTOM)  #  put bottom of next window close to me
	addbutton(root,RIGHT)  #  put right to next widget close to me
	addbutton(root,BOTTOM)  #  put bottom of next widget close to me
	
	root.mainloop()  # start the event loop
	
main()