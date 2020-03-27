#this is a sample python program that uses branches and functions to 
#create a small blind games creating options to select by the user

from sys import exit

def gold_room():
	print 'this room is full of gold , how much do you take ?'
	
	choice=raw_input('> ')
	if '0' in choice or '1' in choice:
		how_much=int(choice)
	else:
		dead('Man , learn from their mistake')
		
	if how_much<50:
		print 'Nice, you are a very greedy person !'
		exit(0)
	else:
		dead('you greedy bastard!')
		
def bear_room():
	print 'there is a bear here.'
	print 'the bear has a bunch of honey'
	print 'the fat bear is i front of another door.'
	print 'how are you going to move the bear ?'
	bear_moved=false
	
	while true:
		choice=raw_input('> ')
		
		if choice=='take honey':
			dead('the bear looks at you then slaps your face off.')
		elif choice=='taunt bear' and not bear_moved:
			print 'the bear has moved from the foor. you can go through if now.'
			bear_moved=true
		elif choice=='taunt bear' and bear_moved:
			dead('the bear gets pissed off and chews your leg off.')
		elif choice=='open door' and bear_moved:
			gold_room()
		else:
			print 'i got no idea what that means.'
def bathroom():
	print 'here you see the great evil bathroom.'
	print 'he,this is really stupid and may go insane.'
	print 'do you  flee for your life of eat your head .'
	
	choice=raw_input('> ')
	
	if 'flee' in choice:
		start()
	elif 'head' in choice:
		dead('well that was tasty !')
	else:
		bathroom()

def dead(why):
	print why,'\nGAME OVER!'
	exit(0)
	
def start():
	print 'you are in a dark room'
	print 'there is a door to you right and left'
	print 'which one fo you take ?'

	choice=raw_input('> ')

	if choice=='left':
		bear_room()
	elif choice=='right':
		bathroom()
	else:
		dead('you stubmle around the room until you starve.')
		
start()