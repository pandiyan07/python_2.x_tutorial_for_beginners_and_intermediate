# this is a sample python script program which is used to demonstrate the difference between matching and searching using regular #expression

import re

line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
searchObj = re.search( r'dogs', line, re.M|re.I)

if matchObj:															#  this is the matching block .
   print "\nmatch --> matchObj.group() : ", matchObj.group()
else:
   print "\nThe match was not found !!"

if searchObj:															# this is the searching block .
   print "\nsearch --> searchObj.group() : ", searchObj.group()
   print"\n"
else:
   print "Nothing found !!"
