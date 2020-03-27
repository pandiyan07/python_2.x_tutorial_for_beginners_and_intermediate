# this sample python script program is created to demonstrate the pickle , a standard module , giving a demonstration.

import pickle

# the file where we will store the following object.
shoplistfile='shoplist.data'
# the list of things to be bought
shoplist=['apple','mango','grapes']

# write to the file in binary mode
f=open(shoplistfile,'wb')
# dumping the object to a file named to be 'f'
pickle.dump(shoplist,f)
f.close()

# destroying the shoplist variable
del shoplist

# reading the object to again from the file.
f=open(shoplistfile,'rb')
# load the object from the file.
newlist=pickle.load(f)


print newlist

# this is the end of the python program . happy coding ..!!