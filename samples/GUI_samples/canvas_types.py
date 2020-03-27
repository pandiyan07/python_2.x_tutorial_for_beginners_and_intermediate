# this is a sample python script program  which is used to demonstrate the concept of using the canvas in the python GUI progamming.

from Tkinter import *

root=Tk()

canvas=Canvas(root,width=400,height=400)
canvas.create_oval(10,10,100,100,fill='red')
#		canvas.create_line(105,10,200,105,stipple='@bitmaps/gray3'
#																				 the above line is showing @bitmaps/gray3 error and is not accepting the value
canvas.create_rectangle(205,10,300,105,outline='white',fill='gray50')
canvas.create_bitmap(355,53,bitmap='questhead')

xy=10,105,100,200

canvas.create_arc(xy,start=0,extent=270,fill='gray60')

canvas.create_arc(xy,start=270,extent=5,fill='gray70')

canvas.create_arc(xy,start=275,extent=35,fill='gray80')

canvas.create_arc(xy,start=310,extent=49,fill='gray90')

canvas.create_polygon(205,105,285,125,166,177,210,199,205,105,fill='white')

canvas.create_text(350,150,text='pandiyan',fill='yellow',font=('verdana',36))

img=PhotoImage(file='globe.gif')
canvas.create_image(145,280,image=img,anchor=CENTER)

frm=Frame (canvas,relief=GROOVE,borderwidth=2)
Label(frm,text='Embeded Frame/Label').pack()
canvas.create_window(285,280,window=frm,anchor=CENTER)
canvas.pack()

root.mainloop()

# this is the end of the program file. happy coding..!!