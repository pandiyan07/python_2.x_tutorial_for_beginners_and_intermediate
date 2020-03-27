# this is a sample python script program which is used to demonstrate the sorted function used in the list in python scripting language.

basket=['apple','zorrow','mango','banana','grapes','pineapple','eggs']

print'the below presented content is a sorted list'

for i in sorted(basket):
	print i
	
print'the below presented content is a sorted list which is displayed in the form of set'

for i in sorted(set(basket)):
	print i

print'\n well you see in the above two examples, that there is no difference.\n'	

print sorted(set(basket))

# this is the end of the program file . happy coding..!!