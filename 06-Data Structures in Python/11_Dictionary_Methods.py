cgps = {'Arin':3.33,'Nayem':3.03,'Murad':3.22,'Junayed':3.81}
print(cgps)
print(" ")


print(cgps.keys()) # we can print the keys separately , using keys() , it'll return keys as list formate
print(cgps.values()) # we can also print the values separately , using values() , it'll return values as list formate
print(cgps.items()) # it'll return key-value pairs as tuple formate in list
print(" ")


# we can remove any key-value pair, using pop() method and inside this method,we've to use keys
cgps.pop('Junayed')
print('After pop() method: ')
print(cgps)
print(" ")


# we can clear all key-value pairs from a dictionary and convert it in an  empty dictionary
d = {'name':"Arin",'roll':758572,'dept':"CST",'last_cg':3.33,'is_married':False}
d.clear()
print("After clear() method: ")
print(d, type(d))