# this is a sample python script program which is created to demonstrate the nature of class and object variables

class robot:
	"""represents the robot with a name."""
	# this is a class variable which is created to count the number of robots.
	population=0
	
	def __init__(self,name):
		"""initializes the data"""
		self.name=name
		print"\nInitializing {} robots\n".format(self.name)
		
		# when the person is created, the robot.
		# adds to the population
		robot.population+=1
	
	def die(self):
		"""Iam terminating."""
		print" {} is being destroyed !".format(self.name)
		
		robot.population-=1
		
		if robot.population==0:
			print' {} was a last one.'.format(self.name)
		else:
			print'There are still {:d} robots working.'.format(robot.population)
		
	def say_hi(self):
		""" greetings given by the robot
		yes you can definitely do that"""
		print'greetings, my master call me {}.'.format(self.name)
		
	@classmethod
	
	def how_many(cls):
		"""prints the current population"""
		print"we have {:d} robots".format(cls.population)

droid1=robot("A-class")
droid1.say_hi()
robot.how_many()

droid2=robot("B-class")
droid2.say_hi()
robot.how_many()

print'\n The robots can do some work over here'
print'Now the robots have finished their job , so lets destroy them.'
droid1.die()
droid2.die()

robot.how_many()

# this is the end of the file . happy coding..!!
