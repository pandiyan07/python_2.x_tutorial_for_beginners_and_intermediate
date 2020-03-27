# this is a sample python script program which is used to demonstrate the types of relief in the frames concept 
# which is used to apply different types of buttons in the GUI designing in  python
# borderwidth is for the thickness of the each frame 
# width is for  the total  width of the window
# both the pads are the distance to be maintained by the small frames from the window outline

from Tkinter import *

root=Tk()

for relief in [RAISED,SUNKEN,FLAT,RIDGE,GROOVE,SOLID]:
	
	f=Frame(root,borderwidth=5,relief=relief)
	Label(f,text=relief,width=5).pack(side=LEFT)
	f.pack(side=BOTTOM,padx=5,pady=30)
	
root.mainloop()

# this is the end of the program file . happy coding..!!