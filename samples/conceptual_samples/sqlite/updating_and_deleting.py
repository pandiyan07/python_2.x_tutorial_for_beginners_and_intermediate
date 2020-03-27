# this is a sample python program which is used to demonstrate updating and deleting a data in a sqlite database

import sqlite3

db=sqlite3.connect('mydb')
cursor=db.cursor()

cursor.execute('''SELECT name,email,phone FROM users WHERE id=1''')
print'\ninitially : '
print cursor.fetchone()

# Update user with id 1
newphone = '3113093164'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''', (newphone, userid))
cursor.execute('''SELECT name,email,phone FROM users WHERE id=1''')
print'\n\nwhen the row is udated'
print cursor.fetchone()
	
db.rollback()		# this restores all the changes done since the last commit
cursor.execute('''SELECT name,email,phone FROM users WHERE id=1''')
print'\n\nwhen the changes are rolled back'
print cursor.fetchone()

# Delete user with id 2
delete_userid = 2
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
 
db.commit()

db.close()