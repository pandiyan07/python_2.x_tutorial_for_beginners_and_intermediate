# this sample python script program is to demonstarate the for loop concept in the python language

fruits=['apple','mango','grape','orange']
count=[1,2,3,4,5]
change=[1,'diamond',2,'emerald',3,'ruby',4]
# this first kind of for-loop goes through a list
for fruit in fruits:
	print 'a fruit of type: %s' %fruit
	
# the same as above
for number in count:
	print 'this is count %d' %number
	
#now this is a mixed lists in the for loop
# NOTE:	this is a mixed list and we don't know what data type is inside this so

for i in change:
	print 'I got %r' %i
	
# we can also build lists, first start with an empty one
elements=[]

# then use the range function to do 0 to 5 counts

for i in range(0,6):
	print 'adding %d to the list.'%i
	
#append is a function that lists understand

	elements.append(i)
	
#now we can print them out too
for i in elements:
	print 'elements was: %d' %i


#  this is the end of the python program .  Happy coding...!!
