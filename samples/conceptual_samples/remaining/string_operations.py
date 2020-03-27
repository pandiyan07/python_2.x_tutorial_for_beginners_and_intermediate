# this is a sample python script program which is used to demonstrate the string concepts-
# this program consists of some "inbuilt python string functions" which is used to perform
# operations on the strings.

j="this is a sample sentence known as string."
# produce a title.
print"\n\n"
print j.title()
print"_"*100

# produce a upper case
print"\n\n"
print j.upper()
print"_"*100

# produce a lower case
a="PANDiYAN"
print"\n\n"
print j.lower()
print"_"*100

# produce a swapcase effect
b="iAM a PROgraMMer"
print"\n\n"
print b.swapcase()
print"_"*100

# check weather the number is a alphanumeric or not
print"\n\n"
print"the c variable consisits of alphanumeric"
c="iuwhfiwh 737283"
print c
print c.isalnum()
print"_"*100

print"\n\n"
print"the d variable consists of alphanumeric"
d="hdfh82523"
print d
print d.isalnum()
print"_"*100

# check weather the entered string is alphabet or not
print"\n\n"
print'is it a alphabet ?'
f="35636"
print f
print f.isalpha()
print"_"*100

# check weather the entered string is number.
print"\n\n"
print"is it a alphabet ?"
e="pandiyanrox"
print e
print e.isalpha()
print"_"*100

# check weather the entered is title or not
print"\n\n"
print"is it a title ?"
g="Good Morning"
print g
print g.istitle()
print"_"*100

# check weather the entered string is lower case or not.
print"\n\n"
print"is it a lowecase word or not?"
k="pandiyan"
print k
print k.islower()
print"_"*100

# check weather the entered string is upper case or not.
print"\n\n"
print"is it a uppercase or not"
h="SUPER MAN"
print h.isupper()
print"_"*100

# splitting the words.
print"\n\n"
print"now its time to split the words and have fun of this f0llowing sentence = "
s="my name is pandiyan and iam studying in third year computer science and engineering in sasurie college of engineering"
print "\n",s,"\n"
print s.split(" ")
print"_"*100

# joining the splitted words
print"\n\n"
print"now lets join the splitted words:\n"
print " ".join(s.split(" "))
print"_"*100

# searching a word in a sentence.
print"\n\n"
print"now lets find out how many characters far is the given word in the following sentence given below: \n"
print s,"\n"
print s.find("science")
print"_"*100

# to check weather a sentence is starting with the given letter or not..
print"\n\n"
print"now lets check weather the following below given sentence is starting with the given letter or not: \n"
print s,"\n"
print s.startswith("sa")
print"_"*100

# to check  a sentence is ending with the given letter or not
print"\n\n"
print"now lets check weather the following below given sentence is ending with the given letter or not."
print s
print s.endswith("er")
print"_"*100

# this is the end of the python program . happy coding ..!!