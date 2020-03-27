# this is a sample program which is created to demonstrate the continue concept in the python programming language.

while True:
	n=int(raw_input("please enter the number that is to be verified:"))
	if n<0:
		continue # this will take the execution to the beginning of the loop.
	elif n==0:
		break
	print"Square is:",n**2
print"Good bye !"

# this is the end of the program file. happy coding..!!