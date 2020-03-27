# this python script is a string operation module that we have filled it with functions ,
#so that we can use this module in any other file to perform operations using these functions in this file.

def break_words(stuff):
	"""this function will break up the words for us"""
	words=stuff.split()
	return words
	
def sort_words(words):
	"""this function sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	"""prints the first word after popping ot off"""
	word=words.pop(0)
	print word
	
def print_last_word(words):
	"""prints the last word after popping it off."""
	word=words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""take in a full sentence and returns the sorted words."""
	words=break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""prints the first and last words of the sentence"""
	words=break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""this sorts the words then prints the first and last one"""
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# this python module ends over here . happy coding..!!
