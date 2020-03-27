# this is a sample python script program which is created to demonstrate the use of time module
# this program calculates the time taken to respond by the user.

from time import clock

start_time=clock()
name=raw_input('\nPlease enter your name sir.')
elapsed=clock()-start_time
print '\nhello',name,',it took you',elapsed,'seconds to respond\n	'

# this is the end of the program file. happy coding..!!
