# this is a sample python script program which is used to demonstrate the concept of using the property function in the class concept.

# using this property method is more easy and flexible while creating a descriptor method .
class democlass(object):
	count=0
	doc="iam a descriptor class"   # this is a docstring

	def __init__(self,name):
		self.name=name
	
	def setname(self,name):			# the setting function

		# setname always take two arguments and 
		# getname and delname inherits from it
		print"\nsetting the name :",name
		# initialising the name after setting 
		# it for further use inside the democlass		
		self.name=name				

	def getname(self):					# the getting function

		# it takes argument from the setname
		print"\ngetting the name:",self.name
		return self.name

	def delname(self):					# the deleting function

		# it takes argument from the setname
		print"\n deleting the name:",self.name
		del self.name
		

	printer=property(getname,setname,delname,doc)		# the property function
	
def test():
	obj=democlass('pandiyan')		# instantiating the democlass

	print" \nthis name is number one:",obj.printer		
# when you don't assign any value to the obj.printer , the 
# already set value is been forwarded to the getting function
	obj.printer="banana"
# when you give the value to the obj.printer , the newly given
# value is been automatically forwarded to the setting function
	
	print" \nthis name is number two:",obj.printer
	obj.printer="super saiyan"

# deleting the name stored in the obj.printer
	del obj.printer
	
if __name__=='__main__':
	test()

# this is the end of the python program . happy coding ..!!