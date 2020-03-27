# this is a sample python script program which is created to demonstrate my first class program in python.

class pandiyan:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		""" the __init__ method is used to initialise the instance p 
			with assigning the values to the variable a and b
			while instantiating the class  """

	def execute(self):
		print"\n now the execute	 function within the class is executed"
		print self.a,self.b
	
p=pandiyan(3,5)			# instantiating
print "\n\nThis is the value of the instance p :\n",p
p.execute()
print "\n",pandiyan
print "\nIam using the command dir :\n",dir(p)

# this is the end of the python program .happy coding ..!!