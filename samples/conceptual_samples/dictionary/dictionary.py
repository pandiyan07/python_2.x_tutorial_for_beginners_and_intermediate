# this sample python script program is to deomonstrate the functionalities of the dictionaries
# the dictionary can be considered as a advanced type of the list

# create a mapping of state abbreviation
states={
	'delhi':'DL',
	'chattisgarh':'CG',
	'tamil nadu':'TN',
	'west bengal':'WB',
	'andhra pradesh':'AP',
	'kerala':'KL',
	'karnataka':'KR',
	'rajasthan':'RJ',
	'punjab':'PJ'
	}
	
# create a basic set of states and some cities in them
cities={
	'DL':'delhi',
	'CG':'raipur',
	'TN':'chennai',
	'WB':'kolkatta',
	'AP':'hyderabadh',
	'KL':'trivandram',
	'KR':'bangalore',
	'RJ':'jaipur',
	'PJ':'punjab'
	}
	
# print some cities
print'_'*10
print "TN state has:",cities['TN']
print "RJ state has:",cities['RJ']

# print some states
print'_'*10
print"Andhra pradesh's abbreviation is:",states['andhra pradesh']
print"kerala's abbreviation is:", states['karnataka']

#do it by using the state then cities dictionary
print'_'*10
print"Tamil nadu has:", cities[states['tamil nadu']]
print"West bengal has:", cities[states['west bengal']]

# print every state abbreviation
print '_'*10
for state,abbrev in states.items():
	print"%s is abbreviated %s" %(state,abbrev)
	
# print every city in state
print '_'*10
for abbrev,city in cities.items():
	print"%s has the city %s" %(abbrev,city)
	
#now do both at the same time
print '_'*10
for state,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])
	
print'_'*10
# safely get a abbreviation by state that might not be there
state=states.get('Texas')

if not state:
	print"sorry,no texas."
	
#get a city with a default value
city=cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is:%s" %city
print'\n\n'

print'the below contents belongs to the states dictionary.'
print'--- ----- -------- ------- -- --- ------ ----------' 
print states.keys()
print'\n'
print states.values()
print'\n'
print states.items()
print'\n'

print'the below contents belong to the cities dictionary.'
print'--- ----- -------- ------ -- --- ------ ----------'
print cities.keys()
print'\n'
print cities.values()
print'\n'
print cities.items()

# end of the file. happy coding..!!