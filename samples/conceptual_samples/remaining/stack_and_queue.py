# this is a sample python script program that is created to demonstrate the stacks and queue concept.

pandiyan=[1,'python',3,'hacking',7,'vulnerability',9,'exploit']

print'the following line is the list of elements which has been stored in the list name "pandiyan".'
print "> ",pandiyan
print'the below content is a stack pop operation in the list pandiyan'
print "> ",pandiyan.pop() # exploit is been popped out of the list pandiyan
print "> ",pandiyan.pop() # 9 is been popped out of the list pandiyan
print'now lets look at the status of the list.'
print"_"*50
print "> ",pandiyan
print"_"*50
print'adding a new element:',pandiyan.append('fire')
print'> ',pandiyan
print'by now you would have noticed that exploit and 9 is been popped out and a new element fire is been added in the list pandiyan.'

# the STACK follows LIFO - last in first out
# the popping operation takes place from the lastly entered element into the list.
# this kind of elemental access from the list ,
# where last element entered can only be accessed is said to be as the stack.

print'\n\nnow its time to demonstrate the queue concept'
print'the below content is a queue pop operation in the list pandiyan'
print "> ",pandiyan.pop(0) # 1 is been popped out of the pandiyan list.
print "> ",pandiyan.pop(0) # python is been popped out of the pandiyan list.
print'now lets look at the status of the list.'
print'_'*40
print "> ",pandiyan
print'_'*40
print' by now you would have noticed that 1 and python has been popped out of the list pandiyan'

# the QUEUE follows FIFO - first in first out
# the popping operation takes place from the first element of the list.
# this kind of elemental access form the list,
# where the first element entered can only be accessed is said to be as the queue.
