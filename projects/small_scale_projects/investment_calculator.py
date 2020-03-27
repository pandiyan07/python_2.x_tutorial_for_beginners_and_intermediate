# this is a sample python script program which is been created to calculate the investments

amount=float(raw_input("Enter the amount for 1 year:"))
inrate=float(raw_input("Enter the amount of inrate for 1 year:"))
period=float(raw_input("Enter the amount of period(in years):"))
value=0
year=1

while year<=period:
	value=amount+(inrate*amount)
	print"year %d Rs.%.2f" %(year,amount)
	amount=value
	year=year+1
	
# end of the program. happy coding..!!