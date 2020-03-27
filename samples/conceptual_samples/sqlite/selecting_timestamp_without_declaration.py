# this is a sample python program used to demonstrate sqlite's date and datetime types

""" The sqlite3 module uses the column's type to return the correct type of object. 
So, if we need to work with a datetime object, we must declare the column in the table as a timestamp type """

import sqlite3
from datetime import date, datetime

db = sqlite3.connect(':memory:')
cursor= db.cursor()

cursor.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at DATE)''')
# Insert a date object into the database
today = date.today()
cursor.execute('''INSERT INTO example(created_at) VALUES(?)''', (today,))
db.commit()

# Retrieve the inserted object
cursor.execute('''SELECT created_at as "created_at [timestamp]" FROM example'''
row = cursor.fetchone()
print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))

db.close()

# this is the end of the python program . happy coding...!!