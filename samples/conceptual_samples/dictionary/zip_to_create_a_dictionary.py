# this is a sample python script program which is used to demonstrate the usage of zip function and creating a dictionary.

first_sequence=('a','b','c','d','e','f','g','h','i','j')
second_sequence=(9,8,7,6,5,4,3,2,1,0)

forward_dictionary=dict(zip(first_sequence,second_sequence))
reverse_dictionary=dict(zip(second_sequence,first_sequence))

print "\nthis is a forward dictionary :-\n",forward_dictionary
print "\nthis is a reverse type of the above dictionary :-\n",reverse_dictionary

# this is the end of the program file. happy coding..!!