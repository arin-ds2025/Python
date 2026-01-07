def fctril(x):
    fact = 1
    for i in range(1,x+1):
        fact*=i
    print(f"The factorial of {x} is {fact}")
    print(" ")
    
n = 5
m = 6
p = 7
fctril(n)
fctril(m)
fctril(p)

f1 = fctril(3) # this is invalid, can't assign the value in f1 cause that function returns nothing.
f2 = fctril(4) # same
print(f1) # it'll return None
print(f2) # it'll also return None
print(" ")


def greet(name): return f"Hello, {name}.!\nYou're a LoL personality,congrats..!"

print(greet("Nayem")) 
print(" ")
print(greet("Murad"))
print(" ")
print(greet("Shabbir"))
print(" ")

n1 = greet("Shakil") # this is valid, cause that function returns something
n2 = greet("Tania") # same
print(n1)
print(" ")
print(n2)
