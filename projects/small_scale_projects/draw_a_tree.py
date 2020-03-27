# this is a sample python script program which is used to create a program to draw a tree using the python looping statements.

def tree(height):
	row=0
	while row<height:
		count=0
		while count<height-row:
			print(' '),
			count+=1
	
		count=0
		print'*',
		while count<2*row:
			print('*'),
			count+=1
	
		print('\t')
		row+=1
	b=raw_input('>')
	
def main():
	height=int(raw_input("Enter the height of the tree that you want to witness:"))
	tree(height)
	
main()

# this is the end of the program file. happy coding..!!