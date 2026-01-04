num = int(input("Enter a number: "))
fact = 1

for i in range(1,num+1):
    fact*=i

print(f"The factorial of {num} is {fact}")
print(" ")

print(f"The table of {num}: ")
for x in range (1,11):
    print(f"{num} X {x} = {num*x}")