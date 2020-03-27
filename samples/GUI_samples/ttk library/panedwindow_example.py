# this is a sample python program which is used to demonstrate the use of  Paned windows from the ttk library

from Tkinter import *
import ttk

root=Tk()
p = ttk.Panedwindow(root, orient=VERTICAL)
p.pack(fill=BOTH,expand=1)
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)   # second pane

p.add(f1)
p.add(f2)

root.mainloop()

# this is the end of the python program . happy coding....!!