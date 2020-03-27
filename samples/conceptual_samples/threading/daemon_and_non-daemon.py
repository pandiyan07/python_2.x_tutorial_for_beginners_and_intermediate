# this is a sample python script program which is used to demonstrate the daemon and non-daemon thread in python

#  Sometimes programs spawn a thread as a daemon that runs without 
#  blocking the main program from exiting. 

#  Using daemon threads is useful for services where there may not be
# an easy way to interrupt the thread or where letting the thread die in
# the middle of its work does not lose or corrupt data

# If you want a thread to run during execution, but not to keep Python alive once the 
#  other threads have terminated, you can set the Thread's daemon attribute to True.


import threading
import time

def daemon():
 	print '\n',threading.currentThread().getName(),' Starting'
	time.sleep(2)
	print '\n',threading.currentThread().getName(),' Exiting'

# creating and setting the thread as the daemon thread
d = threading.Thread(name='daemon', target=daemon,args=())
d.setDaemon(True)

def non_daemon():
	print '\n',threading.currentThread().getName(),' Starting'
	print '\n',threading.currentThread().getName(),' Exiting'

# creating a non-daemon thread .
t = threading.Thread(name='non-daemon', target=non_daemon,args=())

d.start()
d.join()
t.start()

# this is the end of the python program . happy coding ..!!
