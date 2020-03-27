# This is a sample python script program project which is based on Caesar cipher algorithm .
# which has a sole purpose of encrypting the message given by the user as input.
# this program takes key value and your message for its encryption .

mode=[]
key=[]

def mode_selection():
	
	# the mode_selection() function holds the code for the selection of mode.
	# the mode has 2 options "encryption" and "decryption".
	
	mode_value=raw_input("Do you want to Encrypt or Decrypt the data ?\n>")
	mode.append(mode_value)
	
	if mode[0]=='encrypt':
		key_function()
	elif mode[0]=='decrypt':
		key_function()
	else:
		print'The internal command %s id not recognisable.\nPlease simply enter encrypt or decrypt only !' %mode[0]
		mode_selection()
	

def key_function():
	
	# the key_function() function holds the code for the selection of key value.
	# The key of the value is available in the range of 0 to 25
	
	if mode[0]=='encrypt':
		
		print'\nENCRYPTION MODE initiated....'
		print'---------- ---- ---------'
		key_value=int(raw_input('\n Kindly enter the "key" to Encrypt the data:\n> '))
		key.append(key_value)
		key_validation()
		
	else:
		
		print'\nDECRYPTION MODE initiated....'
		print'---------- --- ---------'
		key_value=int(raw_input('\n Kindly enter the "key" to Decrypt the data:\n> '))
		key.append(key_value)
		key_validation()
	
	
def key_validation():
	
	# the key_validation() function holds the code for the validation of the key value.
	# the given key value by the user as input is checked weather it is within the 0 to 26 range
	
	if key[0]!=range(26):
		input_processor()
	else:
		print'The key value you have entered is a "Invalid" one,so please check the value and re-enter the correct one .'
		#continue
		
def input_processor():

	# the input_processor() function holds the code for getting the message to be encrypted or decrypted,
	# and which is given as input by the user.
	# here the given input is also transformed into upper case before it is sent for the next process
	
	if mode[0]=='encrypt':
		message=raw_input("Please enter the message that you want to encrypt\n> ")
		input=message.upper()
		answer(input,message)
	else:
		message=raw_input("Please enter the message that you want to decrypt\n> ")
		input=message.upper()
		answer(input,message)
	
LETTERS = 'ABCDEFGHIJ KLMNOPQRSTUVWXYZ'


def answer(input,message):

	# the answer() function is the original function where the most important process in the file takes place
	# this function holds the code for encryption and decryption of the input message.
	# it also verifies wheather the given input message only contains the words and not any other symbols or non-alphabetic characters
	
	output=''
	
	for symbol in input:
		
		if symbol in LETTERS:
			num = LETTERS.find(symbol) 					
			
			if mode[0]== 'encrypt':
				num = num + key[0]
			elif mode[0]== 'decrypt':
				num = num - key[0]
				
				
			if num >= len(LETTERS):
				num = num - len(LETTERS)
			elif num < 0:
				num = num + len(LETTERS)
				
			output=output+LETTERS[num]
		
	if symbol not in LETTERS:
		print'\nThe message you have entered "%s" is invalid and cannot be encrypted..!!' %message
		print'Please enter only alphabets ,that is from a to z or A to Z'
		quit(0)
			
	if mode[0]=='encrypt':
		print'\nThe Encrypted message is :'
		print'--- --------- ------- -- -\n\n>\t%s' %output
	else:
		print'\nThe Decrypted message is :'
		print'--- --------- ------- -- -\n\n>\t%s' %output
	
if __name__=='__main__':
	mode_selection()	# the program starts executing here ,as the initiating function is been called..!!

# bullseye baby..!!
# the code works just fine
# has been debugged and a guaranteed as a error free code.
# this type of encryption does not provides any safety.
# so please refer to the caesar cipher version 2.0 .
# this is the end of the program file . happy coding..!!