# 	this is a sample python program which is used to demonstrate the urllib package	and extracting the data and connection code from a 
#	given website url. the data sent by the website will be its source code.

import urllib2

def main():
 	webUrl=urllib2.urlopen("http://google.com")
	print "result code: "+str(webUrl.getcode())
	data=webUrl.read()
	print data

if __name__ == "__main__":
	main()

# this is the end of the python program . happy coding ..!!