class Nothing:
    company = "Asus" # this is class attribute
    
    def __init__(self,name,year,company):
        self.name = name
        self.year = year
        self.company = company # instance attribute
        
n = Nothing("Arin", 2026, "Lenovo")
print(n.name)
print(n.year)
print(n.company) # it'll always print instance attribute whenever it presents
print(" ")

# Object introspection , using dir() method
print(dir(n)) # it'll print all availabe methods for objects as list form
print(" ")

# we can also print that class attribute , though it's also present in constructor as instance attribute
print(Nothing.company)