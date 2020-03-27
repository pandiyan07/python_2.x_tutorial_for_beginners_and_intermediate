#this python program is a sample program for demonstating the raw_input combined with the sys modules

from sys import argv

script,username=argv
prompt='>'

print '\nHi Mr.%s iam the %s script' %(username,script)
print 'If you don\'t mind, I would like to ask you a few questions sir,.'
print '\n\nDo you like me %s ?' %username
likes=raw_input(prompt)

print '\nwhere do you live Mr.%s ?' % username
lives=raw_input(prompt)

print"\nwhat kind of computer do you have Mr.%s ?" % username
computer=raw_input(prompt)

print """Ok then so you said %r about liking me ,You live in %r, not sure where that is. 
		 and you have a %r computer. Good day sir. """ %(likes,lives,computer)

#this is the end of the program file. happy coding..!!