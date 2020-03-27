# this is a sample python script program which is used to demonstrate the filter function in python

# this is the function that will process the queries
def fil(x) : return x>0

# we will use the filter function with function and a sequence as a parameter
# Syntax : filter(aFunction, aSequence)
print list(filter(fil,range(-5,5)))

# this is the end of the python program . happy coding ..!!