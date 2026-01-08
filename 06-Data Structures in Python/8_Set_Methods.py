s = {1,44,2,56,3,5}
print(s)


# we add element using add() method
s.add("Arin")
print(s)


# we remove element using remove() method
s.remove(3)
print(s)
# we can also use discard() method to remove element from a set
'''
    The difference between remove() and discard() methods:
    - if we remove any element from the set using remove() method, it'll through an error
    - if we remove any element from the set using discard() method, it'll not through an error 
'''
# s.remove(69) # it'll through an error and the code will be crashed
s.discard(69) # it means remove 69 from the set, if it is present in the set
print(s)


# pop() method will remove a random element from the set
s.pop()
print(s)