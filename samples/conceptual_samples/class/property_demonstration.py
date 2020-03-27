# this is a sample python script program which is used to demonstrate the
# concept of using the property function in the pythonic class implementation .

class democlass(object):		

# object is a (global) variable. By default it is bound to a built-in class which is the root of the type hierarchy.
# without the (object) the setname function is not working as it uses name instead of self.name

	count=0
	def __init__(self,name):
		self.name=name
	def setname(self,name):			# the setting function
		print"\nsetting the name :",name
		self.name=name
	def getname(self):					# the getting function
		print"\ngetting the name:",self.name
		return self.name
	printer=property(getname,setname)			# the property function
	
def test():
	obj=democlass('pandiyan')		# instantiating the democlass			# first iteration
	print" \nthis name is number one:",obj.printer		
# when you don't assign any value to the obj.printer , the 
# already set value is been forwarded to the getting function
	
	obj.printer="banana"			     # second iteration
# when you give the value to the obj.printer , the newly given
# value is been automatically forwarded to the setting function
	print" \nthis name is number two:",obj.printer
	
	obj.printer="super saiyan"			# third iteration
	print"\n this name is number three:",obj.printer
	
if __name__=='__main__':
	test()

# this is the end of the python program . happy coding ..!!