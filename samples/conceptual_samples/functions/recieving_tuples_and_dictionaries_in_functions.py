# this is a sample python script program which is created to demonstrate the concept of recieving tuples and dictionaries in functions.

def powersum(power,*args):
	# return the sum of each argument raised to the specified power.
	total=0
	for i in args:
		total += pow(i,power)
	return total
	
a=powersum(2,3,4)
print a

# NOTE : *args can be used to recieve the dictionaries in functions.
# this is the end of the program file . happy coding..!!