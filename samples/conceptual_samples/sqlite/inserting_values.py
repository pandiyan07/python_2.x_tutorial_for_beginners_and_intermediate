# this is a sample python program used to insert the given data into  a table

import sqlite3

db=sqlite3.connect('mydb')
cursor = db.cursor()

name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
password1 = '12345'
 
name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'
 
# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
print'First user inserted'
 
# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
print'Second user inserted'
 
"""
# use  executemany command on a list of tuples to insert multiple values into a given table
# the above insertion of user 1 and 2 can be done in a single step using executemany command 

users = [(name1,phone1, email1, password1),  (name2,phone2, email2, password2),  (name3,phone3, email3, password3)]
cursor.executemany(''' INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', users)

#  NOTE : Each element of the sequence must be a tuple.
"""

#  to get the id of the row you just inserted
print'the last row id is',cursor.lastrowid

db.commit()

db.close()

# this is the end of the python program. happy coding...!!