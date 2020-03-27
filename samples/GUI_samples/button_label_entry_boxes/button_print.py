# this is a sample python script program which is used to demonstrate the concept of pushing button and their corresponding actions.

from Tkinter import *

def buttonpushed():
	print'The exit button has been pushed'
	
root=Tk()  #create the root (base) window where all the widgets go.

w=Label(root,text="""a very good morning folks..!!,\n the button below when pushed will display a message,
	in the command prompt respectively.""") # creating a label with words
w.pack() # push the label into the window.

mybutton=Button(root,text="Print",command=buttonpushed)
mybutton.pack()

root.mainloop() #start the loop.

# this is the end of the program file. happy coding..!!