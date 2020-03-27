# this is a sample python script program which is used to demonstrate the
# chain of decorators in python

def bold(f):
	def wrapped():
		return'\n<b>'+str(f())+'</b>'
	return wrapped

def italic(f):
	def wrapped():
		return'<i>'+str(f())+'</i>'
	return wrapped

@bold
@italic
def hello():
	return "hello"

print hello()

# this is the end of the python program . happy coding ..!!