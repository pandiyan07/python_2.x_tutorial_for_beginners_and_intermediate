# this sample python script program is to demonstrate the working of the fibnoacci series.

n=int(raw_input("enter the number till which you want to view the fibnoacci series"))
i=0
ini=0
fin=1

print"the Fibnoacci series is :"
print"1,"
while i<=n:
	sum=ini+fin
	print"%d," %sum
	ini=fin
	fin=sum
	i+=1
	
# this is the end of the program file. happy coding..!!