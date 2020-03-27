# this is a sample python script program which is used to demonstrate the **kwargs in python

def table_things(**kwargs):
	for name, value in kwargs.items():
		print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')

# this is the end of the python program . happy coding ..!!
