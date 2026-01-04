'''
    Types of operators:
    
    1. Arithmetic Operators: Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), Exponentiation(**), Floor Division(//)
               
    2. Comparison Operators: Equal(==), Not equal(!=), Greater than(>), Less than(<), Greater than or equal(>=), Less than or equal(<=)
                                                       
    3. Logical Operators: and,or,not
    
    4. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
    
    5. Membership Operators: in, not in
    
    6. Identity Operators: is, is not
'''

# Arithmetic Operators:
print("2**3: ",2**3)
print("5//2: ",5//2)
print("7%3: ",7%3)
print(" ")

# Comparison Operators: (it'll return boolean value)
print("6==3: ",6==3)
print("2!=2.0",2!=2.0)
print("9>=9: ",9>=9)
print(" ")

# Logical Operators: (it'll return boolean value)
print("3>2 and 4<5: ",3>2 and 4<5)
print("3<2 or 4<5: ",3<2 or 4<5)
print(" ")

# Assignment Operators:
a = 3
a**=4
print("a: ",a)
print(" ")

# Membership Operator: (it'll return boolean value)
ls = [1,2,3,4,5]
print("6 not in ls: ",6 not in ls)
print("4 in ls: ", 4 in ls)
print(" ")

# Identity Operator: (it'll return boolean value)
a = 55
b = "55"
print("a is b: ", a is b)
print("a is not b: ", a is not b)