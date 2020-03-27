""" this is a sample python program which is used to replicate the actions of the calculator."""

print """                        ++++++++++++++++++++++++++++++++
                        ++++++++++++++++++++++++++++++++
													         _/\_   The PYTHON PANDI Calculator V1.0   _/\_
                        ++++++++++++++++++++++++++++++++
	                ++++++++++++++++++++++++++++++++
"""
print """
NOTE : This program has the following restrictions that must be strictly followed for the 
proper functioning of the calculator, as  a very low level algorithm has been used to 
design the backend of the calculator.
			
	The restrictions are :-
		(i)    Only addition can be performed
		(ii)   The input given must be only of single digit (from  0 to 9) 
"""

x=0
b=0
d=0
e=0
y=0
m=0
g=0
h=0
z=0
k=0
l=0
i=0
j=i+1
iter=0

print'\n\t* Please enter to perform a ADDITION *'
a=raw_input("\t> ")
a=list(a)

n=len(a)-1
n=n/2
length=len(a)-n

def result():
	print '\n\n\t -> The ANSWER is "',z,'" <-'
	print '\n  _/\_Thank you for using the calculator. _/\_'
	print'\tYours lovingly Python pandi..!!\n\n\n'
	exit()
	
def  validator(j):
	
	if j==length+1:
		result()
	else:
		main()
		
def main():
	
	global x,b,d,e,i,j,y,k,l,g,h,m
	value=['+']
	c=[]
	f=[]
	
	while True:
		if a[i] not in value:
			a[i]=int(a[i])
			if a[j] in value:
				if k==0:
					y=a[i]
					k+=1
					final(y)
				else:
					c.append(i)
					e=int(c[d])
					e=e+2+x
					a[e]=int(a[e])
					y=a[e]
					x+=2
					final(y)
		else:
			a[j]=int(a[j])
			if l==0:
				y=a[j]
				l+=1
				final(y)
			else:
				f.append(j)
				h=int(f[g])
				h=h+2+m
				a[h]=int(a[h])
				y=a[h]
				m+=2
				final(y)
	
def final(y):
	
	global i,j,z,iter
	
	iter+=1
	z=z+y
	i+=1
	j+=1
	validator(j)

def retry():
	try:
		validator(j)
	except IndexError,ValueError:
		print"\nThere  is a ERROR in your Input"
		print"-----  -- - ----- -- ---- -----"
		print"* Sorry to say that the input you have given is \" NOT A VALID INPUT..!! \""
		print"* Please Retry with a valid input and try to follow the conditions that are mentioned above"
		print"\tfor the proper functioning of the calculator."
		print"* You have to give the input in this format, for example :- 1+2+3"# this is the end of the program file . Happy coding..!!
		get=raw_input("\n-> So do you want to RETRY ?? <- \n(Enter y/n only...!!) :")
		if(get=="y"):
			retry()
		else:
			exit()

if __name__=='__main__':			
	retry()

# This is the end of the program file. Happy coding..!
