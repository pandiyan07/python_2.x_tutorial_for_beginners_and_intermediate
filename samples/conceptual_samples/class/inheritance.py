# this is a sample python script program which is created to demonstrate the concept of inheritance in the class

class Baseclass:				
# This is the parent class or the base class of this program
# all the common characters like the name and age is been kept in the parent class
# represent any school member of the school
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print'\nInitialised baseclass schoolmembers list :{}'.format(self.name)
		
	def tell(self):
			"""tell my details"""
			print '\nThe base class in executed here \n'
			print'Name:"{}" Age:"{}"'.format(self.name,self.age),
	
class teacher(Baseclass):				
# the first child class which inherits from the Baseclass
# the individual character of the teacher like salary is kept within this class
# represents a teacher
	def __init__(self,name,age,salary):
		Baseclass.__init__(self,name,age)			
		# calling and importing all the variable declared in the __init__ block of the class Baseclass
		self.salary=salary										
		print'Initialised teacher class:{}'.format(self.name)
		
	def tell(self):
		Baseclass.tell(self)									
		# calling the  importing everything from the tell block of the class Baseclass
		print'Salary:"{}"'.format(self.salary)
		
class student(Baseclass):				
# the second child class which inherits from the Baseclass
# the idividual character of the student like marks is kept within this class
#represents the student
	def __init__(self,name,age,marks):
		Baseclass.__init__(self,name,age)			
		#  calling and importing variables from the __init__ block of the class Baseclass
		self.marks=marks
		print'initialised students class:{}'.format(self.name)
	
	def tell(self):
		Baseclass.tell(self)									
		# calling and importing everything from the tell  block of the class Baseclass
		print'marks:"{}"'.format(self.marks)

# instantiating both the classes		
t=teacher('Mr.Diwan',55,40000)	# instantiating for teacher
s=student('Pandiyan',23,72)		# instantiating for student

#printing a blank line.
print

members =[t,s]
for member in members:
	# works for both teachers and students.
	member.tell()


# this is the end of the python program file. happy coding..!!