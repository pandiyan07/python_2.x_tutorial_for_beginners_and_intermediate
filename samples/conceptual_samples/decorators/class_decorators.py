# this is a sample python program which is used to demonstrate the class decorators in python .

#Note that a function decorated with a class decorator will no longer be considered a "function" 
# from type-checking perspective:

import types			# importing types to check the object data type of the instances

class Decorator(object):
    """Simple decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('\nBefore the function call.')
        print self.func()
        #res = self.func(*args, **kwargs)
        print('\nAfter the function call.\n')
        #return res

@Decorator
def testfunc():
    nice='Inside the function'
    return nice

testfunc()
# Before the function call.
# Inside the function.
# After the function call.

# checking the instance's type
print isinstance(testfunc, types.FunctionType)
# False
print type(testfunc)
# <class '__main__.Decorator'>
print

# this is the end of the python program . happy coding ..!!