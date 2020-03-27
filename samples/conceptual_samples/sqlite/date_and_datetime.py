# this is a sample python program used to demonstrate sqlite's date and datetime types

import sqlite3
from datetime import date, datetime

# we use PARSE_DECLTYPES and PARSE_COLNAMES to return a datetime.date object data type and 
# to stop the date to be returned as a string data type
db = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor= db.cursor()

cursor.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at DATE)''')
# Insert a date object into the database
today = date.today()
cursor.execute('''INSERT INTO example(created_at) VALUES(?)''', (today,))
db.commit()

# Retrieve the inserted object
cursor.execute('''SELECT created_at FROM example''')
row = cursor.fetchone()
print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))

# without PARSE_DECLTYPES and PARSE_COLNAMES the program would return this :
# The date is 2013-04-14 and the datatype is <class 'str'>
# with PARSE_DECLTYPES and PARSE_COLNAMES the program would return this :
# The date is 2013-04-14 and the datatype is <class 'datetime.date'>

db.close()

# this is the end of the python program . happy coding...!!