# this is a sample program to show you the file operations that can be performed in the python language

from sys import argv
script,filename=argv

txt=open(filename)

print 'the filename that you have entered to open it is :%s' %filename;
print 'and the content within the file is......';
print txt.read()
print txt.close()

#the end . happy coding