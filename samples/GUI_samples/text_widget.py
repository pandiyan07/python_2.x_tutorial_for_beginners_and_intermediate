# this is a sample python script program which is used to demonstrate the text widget that is set on the window using the python gui programming with the help of Tkinter library

from Tkinter import *

root=Tk()
root.title("this is a sample text box working representation.")

text=Text(root,height=26,width=50)
scroll=Scrollbar(root,command=text.yview)
text.configure(yscrollcommand=scroll.set)

text.tag_configure('bold_italics',font=('Verdana',12,'bold','italic'))
text.tag_configure('big',font=('Verdana',24,'bold'))
text.tag_configure('color',foreground='blue',font=('Tempus Sans ITC',14))
text.tag_configure('groove',relief=GROOVE,borderwidth=2)
text.tag_bind('bite','<1>',lambda e,t=text: t.insert(END,"I am gonna rip your head off..!!"))
text.insert(END,'what the hell is going on..??')
text.insert(END,"i don't understand anything ",'bold_italics')
text.insert(END,'can i call you frank  ??','big')
text.insert(END,"what has happened to me ??",'color')

text.insert(END,'this is python gui programming','groove')

button=Button(text,text='I do like gossiping with friends')
text.window_create(END,window=button)

photo=PhotoImage(file='globe.gif')
text.image_create(END,image=photo)

text.insert(END,'I dare you click on this ','bite')
text.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)

root.mainloop()
# this is the end of the program file. happy coding..!!