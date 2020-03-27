# this is a sample python script program which has been created to demonstrate the quadratic equation topic

import math

a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
c=int(input("Enter value of C:"))
d=int(input("Enter value of D:"))

if d<0:
	print("roots are imaginary")
else:
	root1=(-b+math.sqrt(d))/(2.0*a)
	root2=(-b-math.sqrt(d))/(2.0*a)
	print
	print "Root 1 =",root1
	print "Root 2 =",root2
	
# this is the end of the python program. happy coding..!!