# this is a sample python script program which is used to demonstrate the descriptor using class method in python

class Desc(object):

	def __init__(self):
		self._name = ''

	def __get__(self, instance, owner):
		print "Getting: %s" % self._name
		return self._name

	def __set__(self, instance, name):
		print "Setting: %s" % name
		self._name = name.title()

	def __delete__(self, instance):
		print "Deleting: %s" %self._name
		del self._name

class Person(object):
	name = Desc()

user=Person()

print "\nnow lets set the name"
# setting the name calls the __set__ method automatically and executes the code within it.
user.name="python pandi"		 

print "\nnow lets get the name"
# calling the descriptor class automatically gets the already set value.
user.name

print "\nits time to delete the value"
# using the del keyword before the getting syntax deletes the value
del user.name

# this is the end of the python program . happy coding ..!!