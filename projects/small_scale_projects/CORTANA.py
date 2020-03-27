# this is a sample python script program to make a conversation with the script ..

from sys import exit
from os.path import exists

# the main menu is for defining the menu contents.
def main_menu():
	print'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print'Hello iam CORTANA ,and iam here at your service sir.'
	print'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print'\nNow, may i know your good name sir ?'
	name=raw_input('Your Name: ')
	print'\n\n\nHello Mr.%s ,A very good morning sir !!' %name
	print'How is your day sir ?'
	cont()

# the cont function is for represent the continuation of the main menu.
def cont():
	status=raw_input()
	if 'fine' in status:
		print'That\'s a great news sir..!! i hope you enjoyed the whole day\n and it must be productive for you'
	else:
		print'Its ok sir ,i know it that you can do it sir...go on !'
	
	print'\nNow shall we proceed sir ?'
	raw_input()
	options()
	
# the options function is for defining the options of the menu.
def options():
	print'\n++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	print'please select any number option so that i can help you.'
	print'+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n'
	print'\n1.How about the latest news'
	print'2.Today is  a great day to start programming - KNOW MORE.'
	print'3.View the sample text file which is located in the pandiyan python library'
	print'4.current status of my life - With Latest updates'
	print'5.Xiaomi is set to launch its note book by next year.- Read full Article'
	selection()

# the selection function is for defining the selction options in the menu by providing the choice to chose
def selection():
	choice=raw_input('> ')
	if (choice=='1'):
		latest_news()
	elif (choice=='2'):
		programming()
	elif (choice=='3'):
		text_file()
	elif (choice=='4'):
		current_status()
	elif (choice=='5'):
		xiaomi()
	else:
		print'Please enter a number option sir, and nothing else.'
		exit(0)
		
# the latest news function is been created is for display the latest news when this option is selected.
def latest_news():
	print'\n\n\n'
	print'LATEST NEWS :-'
	print'====== ==== '
	print'there is no latest news now sir, and we aplogise for the inconvinience that we have caused !'
	print'We request you to please wait patiently , so that we will gather the news for you as soon as'
	print'possible .Loading.......'
	further()
	
# the programming function is been written for display a small content on my programming experience .
def programming():
	print'\n\n\n'
	print'Its a great day to start programming ?'
	print'=== = ===== === == ===== =========== ='
	print'What do you say folks ?'
	print'Well i was saying that it looks like its a good looking day to start coding and the weather '
	print'really suites for it, and i think all of you are with me in matter of my statement made above.'
	print'well you see python is really great language to work with and slowly syncing with it .\n '
		
	print'\tAs all of you know that its dynamic and a very simple language to be understood and used'
	print'which has a lot of potentiality to do a lot. this is the most important factors of python that'
	print'programmers like.Obviously a programming language such a quality can always have a good scope'
	print'of survival and can evolve into a even more stronger one.'
	further()
	
# the text file function is for printing the text files present in the python folder in the C drive.
def text_file():
	print'\n\n\n'
	print'File Viewing'
	print'==== ======='
	print'please enter a text file name that is within the python folder'
	print'in C drive so that i can show you details and print the file content'
	print'on the screen.'
	filename=raw_input('> ')
	txt=open(filename)
	print'\n\n\nAnd the contents in the files are......\n\n'
	print txt.read()
	indata=txt.read()
	print'\n\nDetails about the selected text file'
	print'======= ===== === ======== ==== ===='
	print'\n* The file that you want to view is:%s' %filename
	print'* And precisely the %r file is about %d bytes long.' %(filename,len(indata))
	print'Q: Does the file exists ?\nAns:-%r ..!!' %exists(filename)
	txt.close()
	further()
	
# the current status function is for displaying the current status of the author, and will get activated when the option is selected
def current_status():
	print'\n\n\n'
	print'Current Status'
	print'======= ======\n\n'
	print'There is nothin to be said about at the present .Iam just literally dieing without anything'
	print'without anything and my life really sucks. My PC is not supporting as it has been nearly six '
	print'years that i have bought it and its hardware is not supporting well .The hardware cannot keepup' 
	print'with the latest upgrades that iam making now in the operating systems and its related softwares.'
		
	print'\n\tand on the other hand my parents are so lame that they are not understanding my situation' 
	print'as iam in great need of a good internet connection , as the internet connection that iam using '
	print'now is a just a mobile internet and it totally sucks.'
			
	print'As a conclusion i can only say that the things running around me is purely bullshit.'
	print'WTF man...!?!'
	further()
		
# the xiaomi function is been created for displaying a small content on the xiaomi's products
def xiaomi():
	print'\n\n\n'
	print'Xiaomi\'s Redmi notebook'
	print'========  ===== ========\n\n'
	print'the speculations about the new xiaomi redmi notebook is about to realease seems to be correct'
	print'as the chineese firm has seen a rapid growth in the indian mobile market and it has been started'
	print'its company six years before and has seen a huge profit in the recent years.'
	print'now from mobile the company is set to realease its laptops by the next year ,i.e, in the 2016'
	print'and it has made the indian xiaomi fans very delightful . the most important thing that is to been'
	print'noted is that its configurations . the redmi note has a 16GB ram and i7 skylake processor with a'
	print'1 terrabyte hardisk in just about thirty two thousand only.'
	print'now iam planning to get my hands on it so that i master my programming skills and can make'
	print'myself even stronger.'
	further()

# the further function is been created to show the further actions that must be done after each requested operation by the user
def further():	
	print'\n\nDo you want to go back to option menu or just want to exit cortana ?'
	stat=raw_input('> ')
	if (stat=='menu'):
		print('\n\n\n\n\n\n')
		options()
	elif (stat=='exit'):
		print'\n\n\n\n'
		print'Thank you for using my assistance sir .'
		print'I will be glad if i could do anything more for you sir.'
		print'Anytime and anywhere..!!'
		print'\n\n'
		exit(0)
	else:
		print"Excuse me sir,sorry for interrupting you. Please use only 'menu' and 'exit' as options !"
		further()

main_menu()

# the script ends here.
# Happy coding..!!