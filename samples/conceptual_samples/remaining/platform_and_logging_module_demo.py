# this is a sample python script program which is created to demonstrate the use of platform and logging modules in python.
# using this python script program you can create a log file.
# with details inserted in it.

import os,platform,logging

if platform.platform().startswith('Windows'):
	logging_file=os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'),('test.log'))
else:
	logging_file=os.path.join(os.getenv('HOME'),('test.log'))
	
print'logging to',logging_file

logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s',
filename=logging_file,
filemode='w'
)
	
logging.debug("start of the program")
logging.info("doing something")
logging.warning("terminating now")

# this is the end of the program file . happy coding..!!