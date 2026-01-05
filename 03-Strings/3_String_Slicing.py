email = 'arin2024b@gmail.com'
print("Your user name is: ",email[0:email.index('@')]) # we can get the specific index number of a character in string by index()

# in case of slicing, [start : end : step] .. end and step will be n-1, as like range() function
print(email[0:])
print(email[-1::-1]) # we can manupulate strings by negative indexing.. it will print the string in reverse formate
print(" ")

print(email[0:7:1]) # end will be 6 and step will be 0 , cause both are n-1
print(email[0::2]) # total end and step will be 1