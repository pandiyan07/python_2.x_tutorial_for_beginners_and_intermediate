# this is a sample python script program which is used to demonstrate the concept of the queue module that is used in threading.

import threading
import time
import Queue

exitflag=0

class mythread(threading.Thread):
	
	def __init__(self,threadID,name,q):
		
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.q=q
		
	def run(self):
		print"\nStarting the "+self.name
		process_data(self.name,self.q)
		print"\nExiting "+self.name
		
def process_data(threadname,q):
	while not exitflag:
		
		queueLock.acquire()
		print "hello world"
		if not workQueue.empty():			
			data=q.get()
			queueLock.release()
			print"%s processing %s" %(threadname,data)
		else:
			queueLock.release()
		time.sleep(1)
	
thread_list=["Thread-1","Thread-2","Thread-3"]
name_list=["one","two","three","four","five"]
queueLock=threading.Lock()
workQueue=Queue.Queue(10)
threads=[]
threadID=1

# create new thereads 
for tname in thread_list:
	thread=mythread(threadID,tname,workQueue)
	thread.start()
	threads.append(thread)
	threadID+=1
# fill the queue
queueLock.acquire()

for word in name_list:
	workQueue.put(word)
queueLock.release()

# wait for the queue to empty
#while not workQueue.empty():
#	print"waiting for the queue to get empty"

# notify threads it's time to exit.
exitflag=1

# wait for all threads to complete.
for t in threads:
	t.join()
print"\nexiting the main thread\n"

# this the end of the program file. happy coding...!!
