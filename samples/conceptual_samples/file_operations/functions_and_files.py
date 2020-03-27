# this is a sample python script file which is made to demonstrate the combinations of functions and files together

from sys import argv

script,input_file=argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count,f):
	print line_count,f.readline()
	


# EXECUTION STARTS HERE
	
current_file=open(input_file)

print '\nFirst let\'s print the whole file on the command prompt\'s screen:\n'
print_all(current_file)

print '\nnow let\'s rewind, just like a tape does.\n'
rewind(current_file)			# the cursor is moved to the beginning of the file .

print 'let\'s print about three lines:'

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
print

# this is the end of the pyhon program . happy coding ..!!