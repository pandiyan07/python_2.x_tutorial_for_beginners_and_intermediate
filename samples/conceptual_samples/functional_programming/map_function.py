# this is a sample python script program which is used to demonstrate the map function in python
# the map function perfoms the required operation and save those values in a list

# this is the function that will process the queries
def sqr(x):  return x**2

# we will use the map function with function and a sequence as a parameter
# Synatax : map(aFunction, aSequence)
print map(sqr,range(1,8))

# this is the end of the python program . happy coding ..!!