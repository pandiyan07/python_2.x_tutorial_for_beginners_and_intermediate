# this sample python script program is been created to demonstrate the tuple packing and tuple unpacking.

data=("Name: pandiyan","Wannabe: I want to be a pythoneer","Nationality: indian","Proffession: hacker","Mothertounge: tamil")
name,wannabe,nationality,proffession,mothertounge=data

def details():
	print name
	print wannabe
	print nationality
	print proffession
	print mothertounge
	
print"Are you sure that you want to see my details ..??\t(y/n)"
option=raw_input("> ")
if option=='y':
	details()
elif option=='n':
	print'thank you for opening this file \n now just get lost..!!'
else:
	print"please enter 'y' for yes or enter 'n' for no"

#the end of the program file . happy coding..!!
