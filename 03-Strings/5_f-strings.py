template1 = "Hey {}, You've won {} taka."
a = "Nayem" 
a1 = 240
b = "Mostofa"
b1 = 190
c = "Aryan"
c1 = 970

s1 = template1.format(a,a1)
s2 = template1.format(b,b1)
s3 = template1.format(c,c1)

print(s3) 
print(s2) 
print(s1) 
print("  ")



name = input("Enter your name: ")
cgpa = float(input("Enter your cgpa: "))

template2 = f'''Hey, {name}
You've got cgpa {cgpa} in your last semester final.'''

if cgpa < 4.0:
    advice = f"Dear, {name}, You've to do better with ({cgpa}) this cgpa.!"
else: advice = f"Dear {name}, You did a really good job with ({cgpa}) this highest cgpa..!"

print(template2)
print(advice)