# this is a sample python script program which is used to demonstrate the concept of creating a message window in the python gui programming.

from Tkinter import *

root=Tk()
root.title("Message Box")
Message(root,text=""" a very good morning to one and all present over here and reading my message in the message window .
				this is just a sample python message window created by the python gui programming with the help of the Tkinter inbuilt
				library and it has been a great experience to work with these stuff. I am currently undergoing a gui programming course
				in python and this programming file is just a part of it. Thank you for reading it.""",bg='black',fg='ivory',relief=GROOVE).pack(padx=10,pady=10)

root.mainloop()

#  this is end of the program file. happy coding..!!