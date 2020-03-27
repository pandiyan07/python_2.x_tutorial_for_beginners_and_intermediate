# this is a sample python script program which is used to demonstrate the manipulation of the directories using python .

import os


# creating a new directory
os.mkdir("sample_directory")
print"\n a directory called sample directory is been created .\n"

# changing the current directory
os.chdir("/home/thangam/Python/Samples/conceptual_samples/file_operations/sample_directory")
print"\n  creating a new directory...\n"
os.mkdir("nothing here")

# getting the current working directory
print"\n the current working directory is :"
print "\n",os.getcwd()
print"\n"
print os.listdir(os.getcwd())
print"\n"

cv=raw_input("do you want to remove this sample directory ? (y/n)")
if cv is "y":
	os.rmdir("nothing here")	
	os.chdir("..")
	os.rmdir("sample_directory")
else:
	print"ok then its fine"

# this is the end of the python program . happy coding..!!
