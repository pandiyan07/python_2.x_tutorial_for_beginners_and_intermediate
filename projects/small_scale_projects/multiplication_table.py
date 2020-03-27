# this is a sample python script program which is used to create a multiplication table using basic loops.
# this multiplication table is of 10X10

print"	1   2   3   4   5   6   7   8   9   10"
print"	+------------------------------------+"

for row in range(1,11):
	if row<11:
		print" ",
	print row,'|',
	for column in range(1,11):
		product=row*column
		if product<10:
			print'  ',
		if product>9:
			print' ',
		print product,
	print' '
	
# this is the end of the program file.happy coding..!!
