# File: hello1.py
from Tkinter import *
root = Tk() # Create the root (base) window where all widgets go
w = Label(root, text="""\n\nA very good morning folks..!!,\n\n 
	This is my first GUI window,that you are viewing.""") # Create a label with words
w.pack() # Put the label into the window
root.mainloop() # Start the event loop