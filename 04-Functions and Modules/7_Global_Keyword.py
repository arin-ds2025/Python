# 'global' keyword is used to modify the global variable in function

x = 10 # here x is a global variable

print("Outside and before the mod function, x is: ",x)

def mod():
    global x 
    x = 5 # now it's no more local variable after using global keyword
    # so the value of the global variable is changed

mod()
print("Outside and after the mod function, x is: ",x)