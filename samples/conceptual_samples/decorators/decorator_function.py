# this is a sample python script program which is to demonstrate the decorator function in python .

def decoratorfactory(message):
	def decorator(func):
		def wrapped_func(*args, **kwargs):
			print('The decorator wants to tell you: {}'.format(message))
			return func(*args, **kwargs)
		return wrapped_func
	return decorator

@decoratorfactory('Hello World')
def test():
	pass

test()

# this is the end of the python program . happy coding ..!!