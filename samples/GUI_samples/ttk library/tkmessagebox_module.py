# this is a sample python program which is used to demonstrate the tkinter's error and pop up dialog boxes

from Tkinter import *
from tkMessageBox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()
 
# this is the end of the python program. happy coding....!!