# this is a sample python script program which is used to demonstrate the genreating function using the yield keyword .
# yeild returns the function's output one at a time .

def create_counter(n):
	print'create_counter()'
	while True:
		yield n
		print'increment by 1 and the finally the value reaches : ',n
		n += 1

print'\n'
c=create_counter(2)		# c variable is a generator object with the name create_counter
print c

print '\nlets print the first next function'
print next(c),'\n'
print 'lets print the second next function'
print next(c),'\n'
print 'lets print the third next function '
print next(c),'\n'

# this is the end of the python program . happy coding ..!!