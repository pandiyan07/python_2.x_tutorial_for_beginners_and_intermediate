# this is a sample python script program which is created to demonstrate the concept of raising an error in the exceptional handling 
# concept in the python programming.

def sam():
	"this function is a sample function which take in a integer"
	s=raw_input("Enter a number :")
	return s
	exit(0)
	
while True:
	try:
		print sam()
		raise TypeError("You idiot....its a error")
		break
	except:
		print"there is a type error in the code."

# this is the end of the python program . happy coding ..!!