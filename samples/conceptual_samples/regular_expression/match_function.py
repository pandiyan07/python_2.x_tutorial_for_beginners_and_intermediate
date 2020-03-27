#   This is a sample python script which is used to demonstrate the match() function concept in regular expression .

import re

line="cats are smarter than dogs"
matchobj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchobj:
	print"\nmatchobj.group() :",matchobj.group()
	print"matchobj.group(1) :",matchobj.group(1)
	print"matchobj.group(2) :",matchobj.group(2)
	print"matchobj.groups() :",matchobj.groups()
	print
else:
	print"\nNo match found !!\n"

# this is the end of the python program . happy coding...!!
