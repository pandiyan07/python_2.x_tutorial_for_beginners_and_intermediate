# this is a sample python program which is used to demonstrate the *args in python

def print_everything(*args):
	for count, thing in enumerate(args):
		print( '{0}. {1}'.format(count, thing))
		
print_everything('apple', 'banana', 'cabbage')

# this is the end of the python program . happy coding ..!!