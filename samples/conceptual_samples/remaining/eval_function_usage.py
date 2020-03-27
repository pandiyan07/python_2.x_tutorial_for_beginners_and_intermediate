# this is a sample python script program which is used to demonstrate the use of eval function.

x=input('\nenter the input\n')
print type(x)

y=raw_input('\nenter the raw_input\n')
print type(y)

z=int(raw_input('\nenter the integer raw_input\n'))
print type(z)

a,b=input('\nenter the values of a and b which is a of a normal input form :\n')
print a,b
print type(a),type(b)
"""
e,f=raw_input('\nenter the values of e and f which is of a raw_input :\n')
print e,f
print type(e),type(f)
"""
c,d=eval(raw_input('\nenter the eval value of c and d which is of a eval raw_input form :\n'))
print c,d
print type(c),type(d)

# this is the end of the program file. happy coding..!!
