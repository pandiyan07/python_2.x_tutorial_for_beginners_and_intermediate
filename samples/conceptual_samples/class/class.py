# this is a sample python script program which has a sole purpose to demonstrate the init method concept in the python landuage

class song:
	
	def __init__(self,lyrics):		
		self.lyrics=lyrics
		""" The __init__ method initialises the instances "song_object_1" 
			and "song_object_2" of the class song , with whatever value
			 is given as input while instantitation of the class . """

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

# EXECUTION STARTS HERE

song_object_1=song(["happy bday to you","i don't want to get sued","so i will stop right heren\n"])	# instantiation
song_object_2=song(['they rally around the family','with pockets full of shells\n'])				# instantiation

# now its time we print them in these things within the class.

print'\nhere goes the class.\n'

song_object_1.sing_me_a_song()
song_object_2.sing_me_a_song()

print "printing the song class: ",song

# this is the end of the python program .  happy coding ..!!