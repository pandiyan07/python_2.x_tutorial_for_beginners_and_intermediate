# this is a sample python script program which is created to demonstrate the sets concept .

a=set('abcdecaebdcabecbadbebcacbe')
b=set('fgijhifjhifgjhijghgifgjhif')

print'\nNow lets print the set A'
print a 
print'\nnow lets print the operation A-B'
print a-b
print'\nnow lets print the letters available in eiter A or B'
print a|b
print'\nprinting the letters in both A and B'
print a&b
print'\nprinting the letters in A or B ,but not in both.'
print a^b

print "\nanother updating method"
b.update([3,3,3])
print b

print'\nadding the letter q to the set A'
a.add('q')
print a								# the addition of elemtents in the set is not working.

print'\npopping the letter f form the set B'
b.pop()
print b								# the popping of elements in the set is not working.

print '\nupdating a '
a.update({'q'})
print a

print '\nremoving a element from a'
a.remove('q')						# raises a KeyError if the element is not present in the set.
print a

print '\ndiscarding a element from b'
b.discard('b')						# does not raise KeyError on the abscence of the element
print b

# this is the end of the python program . happy coding..!!