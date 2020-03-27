# this is  a sample python program for retrieving data from a given table

import sqlite3

db=sqlite3.connect('mydb')
cursor=db.cursor()

# using fetchone() to retrieve a single row
cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone() #retrieve the first row
print'using the fetchone() ,we get : ',user1[0] #Print the first column retrieved(user's name)

# using fetchall() to retrieve all the rows
all_rows = cursor.fetchall()
print'using the fetchall(), we get : '
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print'{0} : {1}, {2}'.format(row[0], row[1], row[2])

# here the cursor object works as an iterator, invoking fetchall() automatically	without any requirement for us to call it
print'no need to call fetchall() , simply iterating the cursor object can give the exected result : /n/n'
cursor.execute('''SELECT name, email, phone FROM users''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print'{0} : {1}, {2}'.format(row[0], row[1], row[2])

# fetching a row using a particular condition
user_id = 2
cursor.execute('''SELECT name, email, phone FROM users WHERE id=?''', (user_id))
user = cursor.fetchone()
print'when the data is fetched using any particular condition : ',user

db.commit()

db.close()

# this is the end of the python program. happy coding...!!