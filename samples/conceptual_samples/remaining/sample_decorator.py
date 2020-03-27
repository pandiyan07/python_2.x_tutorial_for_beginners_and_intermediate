# this is a sample python script program which is used to demonstrate the decorator function in python
"""
def wrapper_func(function):
	def samp(*args):
		return '\nthe answer is :' + str(function(*args))+'\n'
	return samp

@wrapper_func
def fun(arg):
	return arg*arg

print fun(123)

# this is the end of the python program . happy coding ..!!

"""
def sample():
	return"i love python"

g=sample()
print g
