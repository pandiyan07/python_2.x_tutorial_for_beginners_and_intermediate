# this is a sample python script program which is used to demonstrate the expression vs generative function

# this is a expression using the list comprehension
print "\nthis is the output of the expression"
a = (c * 5 for c in 'Python')
print "\n",list(a)

# the above code written in the form of Generative function below .
def repeat5times(x):
	for c in x:
		yield c * 5

generator=repeat5times('Python')
print"\nthis is the output of the generative function which is same as above :"
print "\n",list(generator),"\n"

# this is the end of the python program . happy coding ..!!