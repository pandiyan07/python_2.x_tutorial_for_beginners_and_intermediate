# this is a sample python script program which is used to demonstrate how to change the position of the pointer using seek function

# opening a file
fo=open("foo.txt","r+")
string=fo.read(10);
print"\nThe string in the file is : ",string

# check the current position
position=fo.tell()
print"\nCurrent file position : ",position

# Repostioning the  pointer at the beginning once again .
position=fo.seek(3,0)		# fo.seek[offset , from]	- offset is the sarting postion -  from may have 0,1 or 2 as values
# 0 = reference point at the beginning of file , 1 = reference point at current postion , 2 = reference point at end of file

string=fo.read(10)
print"\nAgain reading the string : ",string
print"\n"

# closing the opened file
fo.close()

# this is the end of the python program . happy coding ..!!