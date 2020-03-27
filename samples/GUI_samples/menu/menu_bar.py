# this is a sample python script program which is used to demonstrate the concept of menu bar with a pull down menu bar in 
# python programming

from Tkinter import *

root=Tk()               # create the root window or base window where all widgets go
menubar=Menu(root)      # create a toplevel menu
filemenu=Menu(menubar)  # creating a pulldown menu, and add it to the menu bar.
                        # the above one is a single menu that has been created

root.title("this is my title portion")

def hello():										
	print' a very good morning folks..!!'


filemenu.insert_command(index=1,label='open',command=hello)   #  call the hello function when the open menu is choosen
filemenu.insert_separator(index=4)                           #  add a line separator in the menu
filemenu.insert_command(index=2,label="good one",command=hello)
filemenu.insert_command(index=3,label="exit",command=root.destroy)  #  call the root.destroy function when the exit menu option choosen
menubar.insert_cascade(index=0,label='file',menu=filemenu)    #  add the filemenu as a menu item under the menubar
root.config(menu=menubar)                          #  tell the root window to use your menubar insted of default
root.mainloop()                                    #  start the event loop.

# this is the end of the program file . happy coding..!!