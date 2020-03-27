# this is a sample python program to make a demostration on the topic of functions and their uses

#this one is like your scripts with argv

def print_two(*args):
# the *args written above is just like the argv parameter asking the function to create a required amount of arguments
	arg1,arg2=args
	print "arg1:%r,arg2:%r" %(arg1,arg2)

# ok,that *args is actually pointless , we can just do this

def print_two_again(arg1,arg2):
	print "arg1 : %r , arg2 : %r" %(arg1,arg2)

#this just takes one argument

def print_one(arg1):
	print "arg1:%r" %arg1
	
# this one takes no argument

def print_none():
	print"Sorry guys , i have got nothing to print here"
	
print_two("pandiyan","the king")
print_two_again("pandiyan","the superhero")
print_one("first !")
print_none()

#the end.happy coding..!!