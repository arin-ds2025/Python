def sum(a,b):
    '''This will return the sum of those given arguments'''
    ''' Another one..!LoL ''' # but this will be not accessed.. only first one will be accessed
    return a+b

print(sum(4,5))
print(" ")

# we can also access that ''' ''' comment using __doc__ 
print(sum.__doc__)