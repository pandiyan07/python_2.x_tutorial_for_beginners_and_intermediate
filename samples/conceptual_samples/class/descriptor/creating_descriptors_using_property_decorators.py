# this is a sample python script program which is used to demonstrate 
# the creation of descriptors using property decorators .

class Person(object):

	def __init__(self,_name):
		self._name = ''

	@property
	def name(self):
		print "-> Getting : ",self._name
		return self._name

	@name.setter
	def name(self, value):
		print "-> Setting : ",value
		self._name = value.title()

	@name.deleter
	def name(self,instance):
		print "-> Deleting : ",self._name
		del self._name

	prop=property(name,name.setter,name.deleter)

	
per=Person()


per.prop="pandiyan"			# setting
per.prop					# getting
del per.prop				# deleting

# this is the end of the python program . happy coding ..!!