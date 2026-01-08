ls = [44,59,82,60.4,20,3,True]
print(ls)


# we can add new elements at the end of the list using append() method
ls.append(False) # this will change the original list
print(ls)


# we can insert a list elements into another list at last, using extend() method
ls_ex = [2,5,8,0]
ls.extend(ls_ex)
print(ls)


# we can insert an element in any index of a list, using insert() method
ls.insert(1,"Arin") # at index 1, "Arin" has inserted
print(ls)


# we can remove last element of the list using pop() method
ls.pop() # this will change the original list
print(ls)


# we can remove specific item from  list, using remove() method
ls.remove(60.4) # if the value is not present in the list then it'll through ValueError
print(ls)

print(" ")


lnum = [1,4,2,7,3,5,0,9]
print(lnum)


# we can sort the list using sort() method
lnum.sort()
print(lnum)


# we can reverse the list using reverse() method
lnum.reverse()
print(lnum)


# we can get the size of the list by len() function
cnt = len(lnum)
print(cnt)