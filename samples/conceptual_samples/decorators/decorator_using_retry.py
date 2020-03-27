# this is a sample python script program which created to demonstrate the concept of decorator in the python . here we use retry decorator

from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log=logging.getLogger("retry")

def retry(f):
	@wraps(f)
	def wrapped_f(*args,**kargs):
		MAX_ATTEMPTS=5
		for attempt in range(1,MAX_ATTEMPTS+1):
			try:
				return f(*args,**kargs)
			except:
				log.exception("attempt %s/%s failed : %s",attempt,MAX_ATTEMPTS,(args,kargs))
				sleep(10*attempt)
		log.critical("all %s attempts failed:%s",MAX_ATTEMPTS,(args,kargs))
	return wrapped_f
	
counter=0

@retry
def save_to_database(arg):
	print'\nwrite to a database or make a network call etc.'
	print'this will be automatically retired if exception is thrown\n'
	global counter
	counter+=1
	# This will throw an exception in the first call.
	# and then will work fine in the second call. and it can be said as retry.
	if counter<2:
		raise ValueError(arg)
	
if __name__=='__main__':
	save_to_database("some bad value")
	
# this is the end of the program file. happy coding..!!