# this is a sample python script program which is used to demonstrate the decorator function in python

def wrapper_func(function):
	def samp(args):
		return '\nthe answer is :' + str(function(args))+'\n'
	return samp

@wrapper_func		# the value returned by the fun function will be sent to wrapper_func
def fun(argument):
	return argument*argument

print fun(123)

# this is the end of the python program . happy coding ..!!