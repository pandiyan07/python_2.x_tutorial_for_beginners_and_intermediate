import Tkinter as tk

class application(tk.Frame):
	
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		self.grid()
		self.createwidgets()
		
	def createwidgets(self):
		self.quitbutton=tk.Button(self,text="Quit",command=self.quit)
		self.quitbutton.grid()
		
app=application()
app.master.title('sample appliction')
app.mainloop()