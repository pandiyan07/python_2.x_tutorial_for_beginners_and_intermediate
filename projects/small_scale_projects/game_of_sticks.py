# this is a sample python script program which has been created to demonstrate the game of sticks
# in this game you can't never win the computer as it is disigned in that way.

print"There are 21 sticks and you have to take from 1 to 4 any from it at a time."
print"who ever will take the last stick will loose the game"
sticks=22
sticks_taken=range(1,22)

while True:
	print"Sticks left:",sticks
	sticks_taken=int(raw_input("Choose any one stick from one to four:"))
	if sticks==1:
		print("you took the last stick, so you loose the game")
		break
	if sticks_taken>=5 or sticks_taken<=0:
		print"wrong choice:"
		continue
	print"Computer took:",5-sticks_taken
	print"\n"
	sticks-=5

# this program file ends here . happy coding..!!