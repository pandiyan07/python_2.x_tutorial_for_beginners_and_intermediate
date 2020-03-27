#  this is a sample python program which is used to demonstrate the Basic Polymorphism
#  Polymorphism is the ability to perform an action on an object regardless of its type.

class Shape:
	#This is a parent class that is intended to be inherited by other classes
	def calcarea(self):
        	# This method is intended to be overridden in subclasses.
        	# If a subclass doesn't implement it but it is called, NotImplemented error will be raised.
		print"hello world"
		pass


class Square(Shape):
	#This is a subclass of the Shape class, and represents a square
	global side_length
	side_length = 2     # in this example, the sides are 2 units long
	
	def calcarea(self):
		# This method overrides Shape.calculate_area(). When an object of type
		# Square has its calculate_area() method called, this is the method that
		# will be called, rather than the parent class' version.

		# It performs the calculation necessary for this shape, a square, and
		# returns the result.
		return side_length * 2


class Triangle(Shape):
	# This is also a subclass of the Shape class, and it represents a triangle
	base_length = 4
	height = 3
	def calcarea(self):
		# This method also overrides Shape.calculate_area() and performs the area
		# calculation for a triangle, returning the result.
		return 0.5 * self.base_length * self.height


def get_area(input_obj):
	# This function accepts an input object, and will call that object's
	# calculate_area() method. Note that the object type is not specified. It
	# could be a Square, Triangle, or Shape object.
	print "\n",input_obj.calcarea()


# Create one object of each class
shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()

# Now pass each object, one at a time, to the get_area() function and see the result.
get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)


# this is the end of the python program. happy coding ..!!