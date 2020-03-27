# this sample python script program is to demonstrate the mixture of lists and string concepts.

ten_things='Apples oranges crows telephone light sugar' #this is a sample sentence

print 'wait here are not 10 things in that list. let\'s fix that.'

stuff=ten_things.split(' ')
# stuff is a vairable in which the ten_things sentence is broken into many individual words
more_stuff=['day','night','song','frisbee','corn','banana','girl','boy']
# more_stuff is a list variable where some elements are stored

while len(stuff)!=10:
#the condition of the loop is that the length of the stuff list must be less than of equal to 10
	next_one=more_stuff.pop()
# the next_one is a variable that stores popped elements of the more_stuff list
	print "adding: ",next_one
# printing the current popped element.
	stuff.append(next_one)
# appending the popped element to the stuff variable which has the splitted elements
	print 'there are %d items now' %len(stuff)
# prints the present length of the stuff list item number	
print "there we go:",stuff
# prints the whole new set of elements in the list after appending the popped elements from the more_stuff
print "let's do some things with stuff"

print stuff[1]
# printing the second element of the stuff list;
print stuff[-1]
# printing the last element of the stuff list;
print stuff.pop()
# prints the last element that is popped out of the stuff list.
print ' '.join(stuff)  
# prints the stuff elements that is joined together
print ' and '.join(stuff[3:5]) 
# printing the fourth element and sixth element of the stuff list joined together with a hash mark between them

#end of file.happy coding..!!
