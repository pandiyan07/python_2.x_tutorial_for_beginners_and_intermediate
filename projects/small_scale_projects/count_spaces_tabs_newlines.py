# this is a sample python script program which is created to demonstrate the counting of spaces,tabs and new lines in a file
# while interpreting the script in the command prompt , give the text file to be counted as the file name's argument.

import os
import sys

def parse_file(path):
	"""Parses the text file in the given path will return the count of space ,tab and new line details.
	
	:arg path: path of text file to parse
	
	:return: a tuple with count of spaces,tabs and lines"""
	
	fd=open(path)
	i=0
	spaces=0
	tabs=0
	
	for i,line in enumerate(fd):
		spaces+=line.count(' ')
		tabs+=line.count('/t')
		
		# now lets close the file.
		fd.close()
		
		# return the result as a tuple
		return spaces,tabs,i+1
		
def main(path):
	"""
	Function which prints counts of spaces,tabs and lines in a file.
	:arg path:path of the text file to parse
	:return:True if the file exists or false."""
	
	if os.path.exists(path):
		lines,tabs,spaces=parse_file(path)
		print"The number of spaces is:%d"%spaces
		print"The number of tabs is:%d"%tabs
		print"The number of lines is:%d"%lines
		print"\n Hey..!!,, This program is giving wrong outputs."
		print"don't believe in its outputs."
	else:
		print"\nsomething is wrong , try something else bro."
		return False
		
if __name__=='__main__':
	if len(sys.argv)>1:
		main(sys.argv[1])
	else:
		sys.exit(-1)
	sys.exit(0)
		
		
# this is the end of the program file . happy coding...!!