# this is a sample python script program which is used to demonstrate the threading module
# TIP :  always use .join()  function when you use lock to synchronise your threads .

import threading

val = 0

def increment():
	global val 
	locker.acquire()
	print "\nInside increment"
	for x in range(100):
		val += 1
	print "\nval is now {} ".format(val)
	locker.release()

locker=threading.Lock()
thread1 = threading.Thread(target=increment, args=())
thread2 = threading.Thread(target=increment, args=())
print"\nstarting thread 1"
thread1.start()
thread1.join()
print"\nstarting thread 2"
thread2.start()
thread2.join() 

# this is the end of the python program . happy coding ..!!
