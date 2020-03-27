# this is a sample python script program which is used to demonstrate the descriptors in python

class RevealAccess(object):
	"""A data descriptor that sets and returns values
 		normally and prints a message logging their access.
	"""

	def __init__(self, initval=None, name='var'):
		self.val = initval
		self.name = name

	def __get__(self, obj, objtype):
		print'Retrieving', self.name
		return self.val

	def __set__(self, obj, val):
		print'\nUpdating', self.name
		self.val = val

class myclass(object):
	x=RevealAccess(10,'var "x"')
	y=5

m=myclass()
print "\nprinting m.x"
print m.x

m.x=20

print "\nprinting m.x again"
print m.x

print "\nnow printing m.y"
print m.y

# this is the end of the python program . happy coding ..!!
