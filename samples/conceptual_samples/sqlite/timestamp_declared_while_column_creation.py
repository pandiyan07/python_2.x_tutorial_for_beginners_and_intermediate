# this is a sample python program which is used to demonstrate the declaration of a column as timestamp type

""" The sqlite3 module uses the column's type to return the correct type of object. 
So, if we need to work with a datetime object, we must declare the column in the table as a timestamp type """

import sqlite3
from datetime import date, datetime

db=sqlite3.connect('':memory:)
cursor=db.cursor()
cursor.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY, created_at timestamp)''')
# Insert a datetime object
now = datetime.now()
cursor.execute('''INSERT INTO example(created_at) VALUES(?)''', (now))
db.commit()

# Retrieve the inserted object
cursor.execute('''SELECT created_at FROM example''')
row = cursor.fetchone()
print('The date is {0} and the datatype is {1}'.format(row[0], type(row[0])))

db.close()

# the program would return
# The date is 2013-04-14 16:29:11.666274 and the datatype is <class 'datetime.datetime'>

# this is the end of the python program. happy coding...!