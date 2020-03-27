# this is a sample python script program which is created to demonstrate the finally statement in the exception handling concept in python.

try:
	fi=open("sample.txt","w")
	res=12/0

except ZeroDivisionError:
	print" Now here we have an error in the division.we suggest you to please recheck it..!!"

finally:
	print"\n So, closing the opened file object...."
	fi.close()
	
# this is the end of the python program . happy coding ...!!