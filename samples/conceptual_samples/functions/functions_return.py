# this sample python script program is for demonstrating the function returning any value

def add(a,b):
	print 'ADDING : %d+%d' %(a,b)
	return a+b
	
def subtract(a,b):
	print 'SUBTRACTING : %d-%d' %(a,b)
	return a-b
	
def multiply(a,b):
	print 'MULTIPLYING : %d+%d' %(a,b)
	return a*b
	
def divide(a,b):
	print 'DIVIDING : %d/%d' %(a,b)
	return a/b
	
print 'Let\'s do some maths with just functions !'

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print '\nAge:%d\nheight:%d\nweight:%d,\nIQ:%d' %(age,height,weight,iq)

#a puzzle for the extra credit , type it it anyway.
print '\nhere is  a puzzle for you'

what=add(age,subtract(height,multiply(weight,divide(iq,2))))
print 'That answer for the puzzle is:%d' %what

# this is the end of the python program. happy coding ...!!