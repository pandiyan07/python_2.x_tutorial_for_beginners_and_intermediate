# this is a sample python script program which is used to demonstrate the concept of basic threading.
# the thread module is a primitive and useless . 
# the threading module can be used instead

import thread
import time

# defining a function for the thread to work according to this function.
def print_time(threadname,delay):
	count=0
	while count<5:
		time.sleep(delay)
		count+=1
		print"\n%s : %s" %(threadname,time.ctime(time.time()))
																                           # this program is not working...please see to it....!!

# create two thread as follows
try:
	thread.start_new_thread(print_time,("Thread-1",2,))
	thread.start_new_thread(print_time,("Thread-2",4,))
except:
	print"Error : Unable to start a thread"

while 1:
	pass

# this is the end of the program file. happy coding...!!
