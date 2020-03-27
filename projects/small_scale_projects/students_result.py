# this is a sample python script program which is been created to 
# calculate the student mark and average and declare their result

n=input("\nEnter the total number of students for whom the result must be prepared :")
languages=('physics','maths','chemistry','biology','english')  # languages is just a list of subjects

def processing():
# this loop is for the n number of students
	for i in range(0,n):
		name=raw_input('\nEnter the name of the students %d:'%(i+1))	# get the name of the students for whom we are preparing the result.
		marks=[]
		
		for x in languages:
			
			abc=int(input('\nEnter the marks of %s in 100:'%x))	#gets the mark for each language
			
			if abc<101:
				marks.append(abc)
			else:
				print"Input invalid..!! Please enter the mark within 100"
				processing()
	
		total=sum(marks)
		total=float(total)
		average=total/5
		print"\n\n%s's total marks :%d"%(name,total)
		print"And %s's average is :%.2f percentage"%(name,average)
		
		if total<166:
			print"Result : "				
			print"\n%s has failed the exam with :%.2f percentage"%(name,average)
			print"resulting in %s's reppearence in the arrear exam."%(name)
			print
		else:
			print"\n%s has passed the exam with :%.2f percentage"%(name,average)
			print
	
try:
	processing()
except NameError,TypeError:
	print" Please enter a number !! "
#except:
#	print"the entered mark is not a number , please try again"
	
	
# this is the end of the program file. happy coding..!!
