# this is a sample python program which is used to demonstrate the use of super in-built function in python

#  object is a (global) variable. By default it is bound to a built-in class which is the root of the type hierarchy.
class This_is_a_very_long_class_name(object):
	def __init__(self):
		pass
 
class Derived(This_is_a_very_long_class_name):
	def __init__(self):
		This_is_a_very_long_class_name.__init__(self)    # inheriting the base class's init function
		
		# the above LOC can also be written using super function : -
		super(Derived,self).__init__()			# inheriting the base class's init function using super function
		
# this is the end of the python program . happy coding ...!!