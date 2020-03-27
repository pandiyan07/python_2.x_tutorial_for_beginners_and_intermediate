# this is a sample python script program which is used to demonstrate the  toplevel concept in the python programming language.
# there are four types :-
# the main toplevel known as root
# child toplevel
# transient toplevel
# toplevel

from  Tkinter import *

""" this program is not working , so please work on it later on , whenever you can. the optionDB file is not found
 and that is what the errror says."""
 
root=Tk()
#root.option_readfile('optionDB')
root.title('this is toplevel')

Label(root,text="This is the main(default) top level").pack(pady	=10)
t1=Toplevel(root)

Label(t1,text='This is a child of root').pack(padx=10,pady=10)
t2=Toplevel(root)

Label(t2,text='This is a transient window of root').pack(padx=10,pady=10)
t2.transient(root)

t3=Toplevel(root,borderwidth=5,bg='blue')
Label(t3,text='No wm decoration has been done',bg='blue',fg='white').pack(padx=10,pady=10)
t3=overriderdirect(1)
t3.geometry('200X70+150+150')

root.mainloop()

# this is the end of the program file . happy coding..!!