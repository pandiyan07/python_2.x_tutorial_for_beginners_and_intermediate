# this is a sample python script program which is used to demonstrate the basic FIFO queue in python

import Queue

q=Queue.Queue()

for i in range(5):
	q.put(i)

while not q.empty():
	print q.get()			# the element that is first put() is been removed by get()

# this is the end of the python program . happy coding..!!
