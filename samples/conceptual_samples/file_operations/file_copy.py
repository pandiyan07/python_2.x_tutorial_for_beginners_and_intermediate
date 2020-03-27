# this is a sample python file to demonstrate the file to file content copying process

from sys import argv
from os.path import exists

script,from_file,to_file=argv

print'copying from %s to %s' %(from_file,to_file)

#we could do these in two or one line.
in_file=open(from_file)
indata=in_file.read()

print'the input file is %d bytes long' %len(indata)

print'does the output file exist ? %r' %exists(to_file)
print'ready , hit return to continue, or ctrl+C to abort.'
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print"alright,all done"

print "Ok man ! now press enter to view the new file and view its contents"
raw_input()
pan=open(to_file)
print pan.read()

out_file.close()
in_file.close()

#the end of the file. happy coding..!!
