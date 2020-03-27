# this is a sample python script program which is created to calculate the factorial of a given input number by the user.

def factorial(n):
	
	if n==0:
		a=1
		return a
	else:
		a=n*factorial(n-1)
		return a

a=0
n=int(raw_input('\nPlease enter the number for which you want to find the factorial.'))
factorial(n)	
print'the factorial of the number {} is : {}'.format(n,factorial(n))

# this is the end of the python program file.happy coding..!!