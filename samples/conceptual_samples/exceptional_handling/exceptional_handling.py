# this is a sample python script program which is created to demonstrate the exceptional handling concept in the python

def get_number():
	"the function returns a float number"
	number=float(input("enter a float number:\n"))
	return number
	exit(0)

while True:
	try:
		print get_number()
		break
	except:
		print"\nYou have entered a wrong value."
		print"\nPlease enter a value that is integer or a float value"
else:
	print"there is a error over here, better be carefully about executing it..!!"
		
# this is the end of the program file. happy coding..!!