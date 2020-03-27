# this is a sample python script program which is used to demosntrate the new threading module to manipulate the threads.

import threading
import time
	
exitflag=0
	
class mythread(threading.Thread):
	
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	
	def run(self):
		print"\nStarting :",self.name
		print_time(self.name,self.counter,5)
		print"Exiting :"+self.name+"\n"

def print_time(threadname,delay,counter):	
	while counter:
		if exitflag:
			print"The thread is about to exit."
			thread.exit()
		time.sleep(delay)
		print"%s : %s" %(threadname,time.ctime(time.time()))
		counter-=1
		
# create new threads
thread1=mythread(1,"Thread-1",1)
print"\nThread 1 created"
thread2=mythread(2,"Thread-2",2)
print"Thread 2 created"

# start new threads
thread1.run()
print"Thread 1 has finished Running"
print "is Thread 1 alive now ? : ",thread1.isAlive(),"\n"
thread2.start()
print"Thread 2  has been started"
print"is Thread 2  alive now ? : ",thread2.isAlive(),"\n"

print "\n The number of active thread objects alive : "threading.activeCount()
print "\n list of all alive thread objects :\n"
"""
while thread2.isAlive():
	if not thread1.isAlive():
		exitFlag=1
"""
print"Exiting Main Thread"

# this is the end of the python program file. happy coding..!!
