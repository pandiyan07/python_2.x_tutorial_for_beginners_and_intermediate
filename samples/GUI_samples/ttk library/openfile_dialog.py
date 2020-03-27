# this is a sample python program which is used to demonstrate the open file dialog using tkinter

from Tkinter import *
from tkFileDialog   import askopenfilename      

def callback():
    name= askopenfilename() 
    print name
    
#errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()

# this is the end of the python program. happy coding..!!