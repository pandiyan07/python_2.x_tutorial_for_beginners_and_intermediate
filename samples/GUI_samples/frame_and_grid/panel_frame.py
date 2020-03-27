# this is a sample python script  which is used to demonstrate the use of relief in the frames to create a panel using the python GUI programming.

from Tkinter import *

root=Tk()

firstframe=Frame(root,width=430,height=100)

secondframe=Frame(firstframe,relief=SUNKEN,borderwidth=1)
Label(secondframe,text="Please any one of the option from the below presented one.").pack(pady=10)

Button(secondframe,text="Ready for the upcoming challenge ?",state=DISABLED).pack(side=LEFT,padx=10,pady=10)
Button(secondframe,text="orelse you just want to give up ?",command=root.quit).pack(side=RIGHT,padx=10,pady=10)

secondframe.place(relx=0.01,rely=0.130,anchor=NW)
Label(firstframe,text="A sample Panel").place(relx=0.06,rely=0.125,anchor=W)

firstframe.pack(padx=0,pady=10)
root.mainloop()

# this is the end of the program file. happy coding..!!