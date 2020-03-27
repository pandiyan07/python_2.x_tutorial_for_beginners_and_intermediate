# this is a sample python script program which  is used to demonstrate the static and
#  class method of calling instances and class in python .using the decorators .

class S:
	
	def __init__(self):
		instan=0		
		S.instan=instan+1
	
	@staticmethod	
	def howmanyinstances(self):
		print '\nthe number of instances created',S.instan

	@classmethod
	def foo(self,msg):
		self.message=msg
		print "\n",self.message

a=S()

# This is the Static method
print "\ncalling using the Static method"
# calling through an class
S.howmanyinstances(S.instan)
# calling through an instance
a.howmanyinstances(S.instan)

#This is the Class method
print "\ncalling using the Class method"
# calling through an instance
a.foo('instance call')
# calling through an class
S.foo('instance call')

# this is the end of the python program . happy coding ..!!
