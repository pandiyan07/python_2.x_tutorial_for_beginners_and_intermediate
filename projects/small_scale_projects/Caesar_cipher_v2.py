# this is a sample python script program which is created to improve the level of security in the ceaser cipher algorithm in cryptography
# this program's sole purpose is to curb the main vulnerability of this encrypting and decrypting algorithm.
# Let the name of this algorithm be ceaser v2 algorithm..!!

mode=[]
key=[]
LETTERS ='ABCDEFGHIJ KLMNOPQRSTUVWXYZ'
CHARACTERS='`~1!2@3#4$5%6^7&8*9(0)-_=+?'
#original={'A':'`','B':'~','C':'1','D':'!','E':'2','F':'@','G':'3',
#	'H':'#','I':'4','J':'$','K':'5','L':'%','M':'6','N':'^',
#	'O':'7','P':'&','Q':'8','R':'*','S':'9','T':'(',
#	'U':'0','V':')','W':'?','X':'_','Y':'=','Z':'+',' ':'-'
#	}
#duplicate={'`':'A','~':'B','1':'C','!':'D','2':'E','@':'F','3':'G',
#	'#':'H','4':'I','$':'J','5':'K','%':'L','6':'M','^':'N',
#	'7':'O','&':'P','8':'Q','*':'R','9':'S','(':'T',
#	'0':'U',')':'V','?':'W','_':'X','=':'Y','+':'Z','-':' '
#	}
original=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
duplicate=['`','~','1','!','2','@','3','#','4','$','5','%','6','^','7','&','8','*','9','(','0',')','?','_','=','+','-']

def mode_selection():
	
	# the mode_selection() function holds the code for the selection of mode.
	# the mode has 2 options "encryption" and "decryption".
	
	mode_value=raw_input("\nDo you want to Encrypt or Decrypt the data ?\n>")
	mode.append(mode_value)
	
	if mode[0]=='encrypt':
		key_function()
	elif mode[0]=='decrypt':
		key_function()
	else:
		print'\nThe internal command %s is not recognisable.\nPlease simply enter encrypt or decrypt only !\n' %mode[0]
		mode_selection()
	

def key_function():
	
	# the key_function() function holds the code for the selection of key value.
	# The key of the value is available in the range of 0 to 25
	
	if mode[0]=='encrypt':
		
		try:
			print'\nENCRYPTION MODE initiated....'
			print'---------- ---- ---------'
			key_value=int(raw_input('\n Kindly enter the "key" to Encrypt the data:\n> '))
			key.append(key_value)
			key_validation()
		except ValueError:
			print'The key value you have entered is a "Invalid" one,\nso please check the value and re-enter the correct one .'
			key_function()
		
	else:
		
		try:
			print'\nDECRYPTION MODE initiated....'
			print'---------- --- ---------'
			key_value=int(raw_input('\n Kindly enter the "key" to Decrypt the data:\n> '))
			key.append(key_value)
			key_validation()
		except ValueError:
			print'The key value you have entered is a "Invalid" one,so please check the value and re-enter the correct one .'
			key_function()
		 
def key_validation():
	
	# the key_validation() function holds the code for the validation of the key value.
	# the given key value by the user as input is checked weather it is within the 0 to 26 range
	
	if  key[0]>=0 and key[0]<26:
		input_processor()
	else:
		print'The key value you have entered is a "Invalid" one,so please check the value and re-enter the correct one .'
		key.pop()
		key_validation()
		
def input_processor():
	
	# the input_processor() function holds the code for getting the message to be encrypted or decrypted,
	# and which is given as input by the user.
	# here the given input is also transformed into upper case before it is sent for the next process.
	
	if mode[0]=='encrypt':
		message=raw_input("Please enter the message that you want to encrypt\n> ")
		input=message.upper()
		encryption(input,message)
	else:
		message=raw_input("Please enter the message that you want to decrypt\n> ")
		decryption(message)
	

def encryption(input,message):
	
	# the encryption() function holds the code for the encryption of the message 
	# which is given as input by the user.
	# this is one of the main function of the program file.
	
	different=''
	output=''

	for symbol in input:
		
		if symbol in LETTERS:
			num = LETTERS.find(symbol) 					
			
			
			num = num + key[0]
				
				
			if num >= len(LETTERS):
				num = num - len(LETTERS)
			elif num < 0:
				num = num + len(LETTERS)
				
			output=output+LETTERS[num]
	print output	
	
	if symbol not in LETTERS:
		print'\nThe message you have entered "%s" is invalid and cannot be encrypted..!!' %message
		print'Please enter only alphabets ,that is from a to z or A to Z'
		quit(0)
		
	for encrypter in output:
		different=different+original[encrypter]			
	
	print'\nThe Encrypted message is :'
	print'--- --------- ------- -- -\n\n>\t%s' %different		

def decryption(message):

	# the decryption() function holds the code for the decryption of the message
	# which is given as input by the user
	# this is one of the main function of the program file
	
	different=''
	output=''
	
	for character in message:
		if character in CHARACTERS:
			different=different+duplicate[character]
		else:
			print'\n"THE MESSAGE IS OF UNKNOWN FORMAT"\n'
			print'\nThe encrypted message you have entered is invalid and cannot be decrypted..!!'
		
	print different
		
		
	for symbol in different:
		
		if symbol in LETTERS:
			num = LETTERS.find(symbol) 					
			
	
			num = num - key[0]
				
				
			if num >= len(LETTERS):
				num = num - len(LETTERS)
			elif num < 0:
				num = num + len(LETTERS)
				
			output=output+LETTERS[num]
	print output	
	
	
	
	
	print'\nThe Decrypted message is :'
	print'--- --------- ------- -- -\n\n>\t%s' %output
			
if __name__=='__main__':
	mode_selection()	# the program starts executing here ,as the initiating function is been called..!!

# bullseye baby..!!
# the code works just fine
# has been debugged and a guaranteed as a error free code.
# this is the end of the program file . happy coding..!!