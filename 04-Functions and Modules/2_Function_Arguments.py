def add(a,b,plus=0): # here plus is a default argument
    return a+b+plus

c = add(4,3.6)
print("c: ",c)
print(" ")
d = add(4,3,2.2) # we can change the default value of the argument by passing value
print("d: ",d)
print(" ")



def greet(name = "Arin"): # name is a default argument
    print(f"Hello {name},\nWelcome to the python world..!")
    print(" ")
    
greet()
greet("Aryan") # we can change the default value of the argument by passing value
print(" ")



# we can manupulate the passing value through argument's variable of the function . this is known as keyword arguments
def multiply(a,b,c=1):
    return a*b*c

m1 = multiply(2,c=3,b=4) 
m2 = multiply(c=2,a=3,b=0.5)
m3 = multiply(a=5,b=3)
print("m1: ",m1)
print("m2: ",m2)
print("m3: ",m3)
print(" ")