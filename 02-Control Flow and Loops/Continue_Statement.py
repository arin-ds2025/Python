x = int(input("Enter the limit: "))

print("In case of even numbers: ")
for i in range(1,2*x+1):
    if(i%2!=0): continue
    print(i,end="<>")
    
print(" ")

print("In case of odd numbers:")
for j in range(1,2*x+1):
    if(j%2==0): continue
    print(j,end="<>")
    