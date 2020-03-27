# this is a sample python script program which is used to create a window holding a widget with a canvas having a image.

from Tkinter import *

root=Tk()
pic=PhotoImage(file="thesaiyanprince.gif")  #  creating a photo image

mycan=Canvas(root,width=400,height=200)
mycan.create_line(0,0,20,10)
mycan.create_line(0,10,20,0,fill="red",dash=(4,4))
mycan.create_image(0,0,anchor=NW,image=pic)

w=Label(root,image=pic) # create a label with image
w.image=pic # keeping a regerence to avoid garbage collection
w.pack()  # putting the label into the window.

root.mainloop()

# this is the end of the program file . happy coding..!!