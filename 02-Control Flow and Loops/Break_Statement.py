n = int(input("Enter the limit of odd numbers: "))
print("For odd numbers: ")
for x in range(1,201):
    if(x%2!=0):
        print(x,end="<->")
    if(x==n): break
    
print(" ")

m = int(input("Enter the limit of even numbers: "))
print("For even numbers: ")
for x in range(1,201):
    if(x%2==0):
        print(x,end="<->")
    if(x==m): break
    
