# this is a sample python script program which is used to create python gui appliction which will be used to capture mouse clicks.

from Tkinter import *

def mouseentered(event):
	button=event.widget
	button.config(text="please click me")
	
def mouseexit(event):
	button=event.widget
	button.config(text="logon")
	
def main():
	global root
	root=Tk()
	root.title("This is the title of the following window")
	b=Button(root,text="logon")
	b.bind("<Enter>",mouseentered)
	b.bind("<Leave>",mouseexit)
	b.pack()
	p=Label(root,text="a very good morning folks to one and all..!!")
	p.pack()
	root.mainloop()
	
main()

# this is the end of the program file. happy coding..!!