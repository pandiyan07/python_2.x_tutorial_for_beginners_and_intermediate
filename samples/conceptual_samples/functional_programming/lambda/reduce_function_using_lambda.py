# this is a sample python script program which is used to demonstrate 
# the reduce function in python using lambda function in it

# reduce function applies the assigned operation on the whole list .
from functools import reduce

print "\n",reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

# this is the end of the python program . happy coding ..!!