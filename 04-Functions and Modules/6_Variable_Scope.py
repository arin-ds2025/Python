'''
    Two types of scopes in python:
    1. Local Scope
    2. Global Scope
'''


def show():
    # print("z in show function, befor reinitialize: ",z)
    z = 1 # here z is a local variable and it'll not work after this function
    print("z in show function, after reinitialize: ",z)
    
z = 7 # here z is a global variable and it's accessable in everywhere
print("z outside of the show function: ",z)
show()