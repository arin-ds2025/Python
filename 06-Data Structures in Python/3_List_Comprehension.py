x = 4
table = []

print(table)

for i in range(1,11):
    table.append(x*i)
    
print(table)
print(" ")

# we can do the same thing through list comprehension in a single line
ls = [5*y for y in range(1,11)]
print(ls)

ls2 = [i**2 for i in range(1,16)]
print(ls2)