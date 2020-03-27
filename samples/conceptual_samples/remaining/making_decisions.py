# this sample python script is to demostrate the making decisions

print 'you enter a dark room with two doors.do you go through door #1 or door #2?'

door=raw_input('> ')

if door=='!':
	print 'there\'s a giant bear here eating a cheese cake. what do you do ?'
	print '1.take the cake.'
	print '2.scream at the bear.'
	
	bear=raw_input('> ')

	if bear=='1':
		print 'the bear eats your face off. Good job !'
	elif bear=='2':
		print 'the bear eats your legs off. Good job !'
	else:
		print 'well,doing %s is probably better. bear runs away.' %bear
	
elif door=='2':
	print 'you stare into the endless abyss at retinal layer'
	print '1.bluberries.'
	print '2.yellow jacket clothespind.'
	print '3.understanding revolvers yellowing melodies.'
	
	insanity=raw_input('> ')
	
	if insanity=='1' or insanity=='2':
		print 'your body survives powered by a mind of crazinesss. Good job !'
	else:
		print 'the insanity rots your eyes into a pool of muck, Good job !'

else:
	print 'you stumble around and fall on a knife and die. Good job !'
	
# this is the end of the python program .happy coding ...!!
	
	
