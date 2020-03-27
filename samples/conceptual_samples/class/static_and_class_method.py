# this is a sample python script program to demonstrate the topic of static method and class method in a python program.

class theclass:
	
	def stat_func(self):
		return 'this is a first function returned statement,\n to demonstrate the static method\n'
	
	def class_func(self):
		return 'this is a second function returned statement,\n to demonstrate the class method: %s'%repr(object)+'\n'
	
	stat_var=staticmethod(stat_func)
	class_var=classmethod(class_func)


# EXECUTION STARTS FROM HERE
	
theobj=theclass()

print("\n")
print theobj.stat_var(theobj)
print theobj.class_func()
print "_"*80
print("\n")
print theclass.stat_var(theclass)
print theclass.class_var()

# this is the end of the python program. happy coding..!!