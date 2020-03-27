# this piece of python script is to get the string operation module imported and perform operations 
# by using the functions that are defined inside that module and performing their specified operaitions in thid file

import string_operation_module

# ->" from string_operation_module import * "<- can also be written instead of above import syntax

sentence='\n all good things come to those who wait.\n'

words=string_operation_module.break_words(sentence)
words

sorted_words=string_operation_module.sort_words(words)
sorted_words

string_operation_module.print_first_word(words)
string_operation_module.print_last_word(words)
words

string_operation_module.print_first_word(sorted_words)
string_operation_module.print_last_word(sorted_words)
sorted_words
sorted_words=string_operation_module.sort_sentence(sentence)
sorted_words
string_operation_module.print_first_and_last(sentence)
string_operation_module.print_first_and_last_sorted(sentence)

# the program ends here and please execute to see 
# the actions that is performed by the string_operaion_module
# as you can see at the top of this file that it has been imported to this file for its use.

#end of file. happy coding..!!