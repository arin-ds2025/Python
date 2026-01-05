name = 'Arin Ahmed'
email = 'arinahmed910@gmail.com'
ht = "thakurgaon sadar"


# we can get the length of a string through len() function
print("Length of email: ",len(email))
print(" ")


'''
    We can change the case of a string , through:
    
    1. name.upper() # output: ARIN AHMED
    2. name.lower() # output: arin ahmed
    3. ht.title() # output: Thakurgaon Sadar .. every separate word's first letter will be in upper case
    4. ht.capitalize() # output: Thakurgaon sadar  .. only first word's first letter will be in upper case
'''
print("name.upper(): ",name.upper())
print("name.lower(): ",name.lower())
print("ht.title(): ",ht.title())
print("ht.capitalize(): ",ht.capitalize())
print(" ")


text = " Hello World "
'''
    we can remove extra whitespaces, using strip() function:
    
    1. text.strip() # output: "Hello World"  .. remove all extra whitespaces
    2. text.lstrip() # output: "Hello World " .. remove only left sided extra whitespaces
    3. text.rstrip() # output: " Hello World" .. remove only right sided extra whitespaces
'''
print("text.strip(): ",text.strip())
print("text.lstrip(): ",text.lstrip())
print("text.rstrip(): ",text.rstrip())
print(" ")


'''
    We can find the first index number of a word through find() function .. it'll return the index number of first letter of the word:
    Example: ht.find('sadar')  # output: 11 .. cause the index number of s in that string is 11
    
    We can find the index number of a single character from a whole string, using index() function:
    Example: email.index"('@') # output: 12
    
    we can replace anything in string , through replace() function:
    Example: 
    1. name.replace('Arin','Aryan') # output: Aryan Ahmed
    2. ht.replace('s','S') # output: thakurgaon Sadar
'''
print("ht.find('sadar'): ",ht.find('sadar'))
print("email.index('@'): ",email.index('@'))
print("name.replace('Arin','Aryan'): ",name.replace('Arin','Aryan'))
print("ht.replace('s','S'): ",ht.replace('s','S'))
print(" ")


ls = "Apple,Banana,Lichi,Mango"
'''
    We can split a string and convert it into list, using split() function
    Example: ls.split(',') # output: ['Apple','Banana','Lichi','Mango']
'''
print("ls.split(','): ",ls.split(','))
print(" ")


cars = ['BMW','HONDA','TOYOTA','BYD','AUDI']
'''
    We can join a list and convert it into string, using "something".join(list) function
    Example: "<>".join(cars)
'''
print(" \"<>\".join(cars): ","<>".join(cars))
print('another one: '," / ".join(['Apple', 'Banana', 'Lichi', 'Mango']))
print(" ")


test = 'pythonV311'
'''
    There another properties of string: (it'll return True or False)
    
    1. test.isalpha() # output: False .. cause there are number also. it should be in all alphabets to get True 
    2. test.isdigit() # output: False .. cause there are aphabets also. it should be in all numbers to get True 
    3. test.isalnum() # output: True .. cause there are mixture of aphabets and digits
    4. test.isspace() # output: False .. cause there are not spaces in that string
'''
print("test.isalpha(): ",test.isalpha())
print("test.isdigit(): ",test.isdigit())
print("test.isalnum(): ",test.isalnum())
print("test.isspace(): ",test.isspace())
print(" ")


'''
    We can get the ascii value of a character, using ord() function
    Example: ord('A') # output: 65
    
    We cam get the character through ascii value, using chr() 
    Example: chr(97) # output: a
'''
print("The ascii value of 'A' is: ", ord('A'))
print("The character of the ascii value 97 is: ",chr(97))