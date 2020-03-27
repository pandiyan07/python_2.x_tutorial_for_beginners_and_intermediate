# this is a sample python program to execute creating and dropping a table

import sqlite3 

# Creates a temproary database in RAM
#db = sqlite3.connect(':memory:')

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydb')

# to perform any operation with the database we need to create a cursor object

cursor = db.cursor()

# command for creating a table
cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, email TEXT unique, password TEXT)''')

# command for dropping or deleting a table
# cursor.execute('''DROP TABLE users''')

db.commit()
db.close()

# this is the end of the python program. happy coding....!!!