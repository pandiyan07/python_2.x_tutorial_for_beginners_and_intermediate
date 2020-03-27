#  this is a sample program which is used to encode a string into hexadecimal and use it for ASCII conversion .

stringName = raw_input("\nConvert string to hex & ascii(type 'stop' to quit): ").strip()
if stringName == 'stop':
	exit(0)
else:   
	print "\nHex value: ", stringName.encode('hex')
	print "ASCII value: ", ', '.join(str(ord(c)) for c in stringName)
	print

# this is the end of the python program . happy coding ..!!
