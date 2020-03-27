# this is a sample python program which is used to create a user defined exception

class MyError(Exception):
	def __init__(self, value):
		self.value = value
		def __str__(self):
			return repr(self.value)

try:
	raise MyError(2*2)
except MyError as e:
	print 'My exception occurred, value:', e.value

# this is the end of the python program . happy coding ...!!!