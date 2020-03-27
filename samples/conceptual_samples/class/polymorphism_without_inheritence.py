# this is a sample python program which is used to demonstrate the Polymorphism without inheritence
# there is no such parent or child classes over here , hence there is no inheritence takes place .
class Duck:
	def quack(self):
		print("Quaaaaaack!")
	def feathers(self):
		print("The duck has white and grey feathers.")

class Person:
	def quack(self):
		print("The person imitates a duck.")
	def feathers(self):
		print("The person takes a feather from the ground and shows it.")
	def name(self):				# this function will not be printed
		print("John Smith")

def in_the_forest(obj):
	obj.quack()
	obj.feathers()

donald = Duck()
john = Person()
in_the_forest(donald)
in_the_forest(john)

# this is the end of the python program . happy coding..!!