# Tuples are ordered but immutable collections of items

tp = ("Arin",2,5,8,0,True,3.67)
print(tp)
print(tp[::-1]) # we can slicing index of tuples
print(tp[4])
#tp[4] = 3.61 # this is not possible cause tuples are immutable
#print(tp)

'''
    Why use tuples..?
    - Faster than list
    - Used as dictionary keys
    - Safe from unintended modifications
'''