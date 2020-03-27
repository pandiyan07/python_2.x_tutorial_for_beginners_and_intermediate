#this is the use of hero

hero="%r %r %r %r"

print hero % (1,2,3,4)
print hero % ('one','two','three','four')
print hero % (True,False,False,True)
print hero % (hero,hero,hero,hero)
print hero % ("this is a sample",
                         "this is a second sample",
                         "it is about hero",
                         "so i said bye and see you soon")
