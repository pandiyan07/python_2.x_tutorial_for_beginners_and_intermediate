# this is a sample python program which is given in the python interpreter documentation on the tkinter module.

import Tkinter
from Tkconstants import *

tk=Tkinter.Tk()

frame=Tkinter.Frame(tk,relief=RIDGE,borderwidth=2)
frame.pack(fill=BOTH,expand=1)

lable=Tkinter.Label(frame,text="Hello world")
lable.pack(fill=X,expand=1)

button=Tkinter.Button(frame,text="exit",command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()

# this is the end of the progam file . happy coding..!!