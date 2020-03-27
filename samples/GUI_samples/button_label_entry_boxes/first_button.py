# this is a sample python script program which is used to demonstrate the concept of buttons in the gui programming in python

from Tkinter import *

root =Tk()  #create the root base window where all widgets go

w=Label(root,text="\nA very good morning folks,\nthis is the first window to demonstrate the button\n") # create a label with set of words.
w.pack()

thebutton=Button(root,text="Voila !") # create a button with words.
thebutton.pack() # put the button into the window

w=Label(root,text="\n")
w.pack() # put the label into the window

root.mainloop() #starting the eventloop