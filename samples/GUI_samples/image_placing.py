# this is a sample python script which is used to demonstrate the concept of image in the window as a widget using the python tkinter.

from Tkinter import *

root=Tk()
pic=PhotoImage(file='globe.gif') #  creating the photoimage widget to place the image in it

# adding the photo to a label
w=Label(root,image=pic)  # creating a label with image
w.image=pic  # always keep a reference to aviod the garbage collection
w.pack()  # put the label into the window

root.mainloop()

#  this is the end of the program file. happy coding..!!