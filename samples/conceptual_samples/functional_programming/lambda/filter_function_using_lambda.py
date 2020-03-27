#  this is a sample python script program which is created to demonstrate the filter inbuilt function which used with lambda function

mylist=[1, 5, 4, 6, 8, 11, 3, 12]

# the whole list is taken to perform the task on certain elements which satisfies the condition specified .
newlist=list(filter(lambda x:(x%2 ==0) , mylist))   
print newlist


#  this is the end of the python program . happy coding...!!
