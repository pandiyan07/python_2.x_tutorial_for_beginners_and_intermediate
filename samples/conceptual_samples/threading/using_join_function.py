# this is a sample python script program which is used to demonstrate the use of .join()   function in python
import threading
import time

def printer():
	for _ in range(3):
		time.sleep(3)
		print "hello"

thread = threading.Thread(name="printing_thread",target=printer,args=())
thread.start()
thread.join()
print "goodbye"

# this is the end of the python program . happy coding ..!!
