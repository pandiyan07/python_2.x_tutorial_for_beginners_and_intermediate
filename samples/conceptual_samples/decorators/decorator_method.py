# this is a sample python script program which is used to demonstrat the decorator method in python

# For decorating methods you need to define an additional __get__-method:

# Class Decorators only produce one instance for a specific function so decorating a method
# with a class decorator will share the same decorator between all instances of that class:

from types import MethodType

class CountCallsDecorator(object):
	def __init__(self, func):
		self.func= func
		self.ncalls = 0    # Number of calls of this method
        
	def __call__(self, *args, **kwargs):
		self.ncalls += 1   # Increment the calls counter
		print self.func(*args, **kwargs)
    
	def __get__(self, instance, cls):
		return self if instance is None else MethodType(self, instance)		# i don't understand MethodType()

class Test(object):
	def __init__(self):
		pass
    
	@CountCallsDecorator
	def do_something(self):
		return 'something was done'
    
a = Test()
a.do_something()
a.do_something.ncalls   # 1
b = Test()
b.do_something()
b.do_something.ncalls   # 2

# this is the end of the python program .  happy coding ..!!