# this is a sample python script program which created to demonstrate the matrix multiplication program.
# this code ain't workin

n=int(raw_input("Enter the order of matrix that is to be multiplied:"))
nsq=n**2
n=nsq
a=raw_input("Enter values for the matrix A\n> ")
a=list(a)
newa=[item for item in  a if item!=" "]

if len(newa)==nsq:
	matrixAprinter()
#for i in range(0,nsq):
#	a.append(a.split("") for x in a if x==range(0,11))

b=raw_input("enter values for the matrix B\n> ")
b=list(b)
newb=[objecto for objecto in b if item!=" "]
#for i in range(0,n):
#	b.append([int(x) for x in input("").split("")])
"""
c=[]

for i in range(0,9):
	c.append([a[i][j]*b[j][i] for j in range(0,9)])

print("After matrix multiplication")
print("-"*10*n)

for x in c:
	
	for y in x:
		print"%5d" %y
	
	print("")

print("-"*10*n)
"""
matrixAprinter()
{
	ak=(nsq)/n
	print"\nThe value of Matrix A is:"
	for ele in range(nsq):
		for line in range(a):
			print newa[ele]
		a+=a
}
# this is the end of the program file. happy coding..!!
