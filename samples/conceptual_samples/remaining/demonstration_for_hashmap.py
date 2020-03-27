# this is a sample python script program which is for demonstrating the dictionary module's workings by importing it in this file

from hashmap import *

# create a mapping of state to abbreviation
states=new()
set(states,'tamilnadu','TN')
set(states,'rajasthan','RJ')
set(states,'kerala','KL')
set(states,'karnataka','KR')
set(states,'andhrapradesh','AP')

# create a basic set of states and some cities in them
cities=new()
set(cities,'KL','kollam')
set(cities,'AP','hyderabadh')
set(cities,'RJ','jaipur')

# add some more cities.
set(cities,'TN','chennai')
set(cities,'KR','bangalore')

# print out some cities
print '-'*10
print'TN state has the capital:%s' % get(cities,'TN')
print'RJ state has the capital:%s' % get(cities,'RJ')

# print some states
print'-'*10
print'The state Tamil nadu\'s abbreviation is %s:' % get(states,'tamilnadu')
print'the state rajasthan\'s abbreviation is:%s' % get(states,'rajasthan')

# do it by using the state then cities dictionary
print'-'*10
print' the state Kerala has:%s' %get(cities,get(states,'kerala'))
print'the state Andhra pradesh has:%s' %get(cities,get(states,'andhrapradesh'))

# print every state abbreviation
print'-'*10
list(states)

# print every city in state 
print'-'*10
list(cities)

print'-'*10
state=get(states,'texas')

if not state:
	print'Sorry, no such state is available in our data structure library .'
	
# default values using ||= with the nil result
# can you do this on one line ?
city=get(cities,'TX','Does not exist')
print'The city for the state \'TX\' is :%s' %city

# end of file. happy coding..!!