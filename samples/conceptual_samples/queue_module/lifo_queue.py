# this is a sample python program which is used to demonstrate the Lifo function in Queue module .
# this is a stack

import Queue

q=Queue.LifoQueue()

for i in range(5):
	q.put(i)

while not q.empty():
	print q.get()			# the element that is been most recently put()  is been removed by get()

# this is the end of the python program . happy coding ..!!
