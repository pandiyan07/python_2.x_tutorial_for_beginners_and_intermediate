# this is a sample python script program which is used to demonstrate the concept of blocking ,locking and releasing a thread

import threading
import time

class mythread(threading.Thread):
	
	def __init__(self,threadID,name,counter):
		
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
		
	def run(self):
		
		print"\nStarting "+self.name
		# get lock to synchronize the threads
		locker.acquire(0)
		# in acquire(blocking) , if blocking is set to 0, the thread returns immediately with 
		# a 0  value if the lock cannot be acquired and with a 1  if the lock was acquired. 
		# If blocking is set to 1, the thread blocks and wait for the lock to be released.
		print_time(self.name,self.counter,3)
		# free lock to release next thread
		locker.release()
		
def print_time(threadname,delay,counter):

	while counter:
		time.sleep(delay)
		print"%s : %s" %(threadname,time.ctime(time.time()))
		counter-=1
		
locker=threading.Lock()
threads=[]
# create new threads
thread1=mythread(1,"Thread-1",1)
thread2=mythread(2,"Thread-2",2)
print "\nthe NEW threads are created"

# Start new threads
thread1.start()
thread2.start()
print"\nthe NEW threads are STARTED"

# add threads to thread list
threads.append(thread1)
threads.append(thread2)
print"\nThe two threads are APPENDED to the list"

# wait for all threads to complete
for t in threads:
	print"\nwaiting for the thread to terminate ."
	t.join()
	print"\nterminating the thread now.\n\n"

print"\nExiting Main Thread\n"

# this is the end of the program file. happy coding..!!
