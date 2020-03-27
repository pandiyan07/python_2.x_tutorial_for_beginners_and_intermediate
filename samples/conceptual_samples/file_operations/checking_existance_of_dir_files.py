# this is a sample python program which is used to demonstrate the using of os module to check if a directory , file exists or not

import os

# we can also use os.path.exists("location_of_a_file_or_directory") for knowing the existance of any file or directory

if not os.path.isdir("C:\Users\MAX"):				#  check the existance of the given directory
	print" The directory 'C:\Users\MAX' does not exist"
else:
	print"Yes ,the directory 'C:\Users\MAX' exists"
	if not os.path.isfile("my_calculator.py"):	# check the existance of the given file name
		print"But iam sorry, the file 'my_calculator.py' does not exists"
	else:
		print"And also the file 'my_calculator.py' exists within the directory"
		
# this is the end of the python program . happy coding...!!