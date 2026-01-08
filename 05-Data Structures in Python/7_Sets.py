# Sets are unordered, unique collections of items

fruits = {'Mango','Banana','Lichi','Cherry'}
print(fruits) # after printing the set, it'll show in unordered form 

nums = {1,2,3,4,3,5,6,3,2,9,7,1,8}
print(nums,type(nums)) # it'll print only unique values and skip duplicates

# we can't indexing in sets, cause sets are not in ordered formate
# print(nums[::-1]) # it'll through an error
# print(fruits[3]) # same