# Dictionaries store key-value pairs and allow fast lookups

d = {'name':"Arin",'roll':758572,'dept':"CST",'last_cg':3.33,'is_married':False}
print(d,type(d))
print(d.keys()) # we can print the keys separately , using keys() 
print(d.values()) # we can also print the values separately , using values()
print(" ")

# Accessing and modifying values:
print("Accessing values, using keys as index:")
print(d['roll'])
print(d['last_cg'])
d['is_married'] = True
d['dept'] = "EEE"
d['last_cg'] = 3.61
print("After modification: ")
print(d)
