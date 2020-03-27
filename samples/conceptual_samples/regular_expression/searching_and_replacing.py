# this is a sample python script program which is used to demonstrate the search and replace concept in regular expression .

import re

phone="2004-959-559 # this is just a random phone number "

# deleting the python styled comments .
num=re.sub(r'#.*$',"",phone)
print"\nThe Phone number after removing the comment is : ",num

# remove anything other than digits
num=re.sub(r'\D',"",phone)
print"\nThe phone number after removing everythin except number is:\n ",num
print"\n"

# this is the end of the python program . happy coding..!!
