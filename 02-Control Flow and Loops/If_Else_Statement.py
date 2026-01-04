name = input("Enter your name: ")
pas = int(input("Enter your password in integers: "))

if(name == 'Arin' and pas == 2580): print("Welcome,Arin Ahmed!\nHope, your day will be good enough")
elif(name != 'Arin' and pas == 2580):
    print("Your name is incorrect, please try again")
    name = input("Enter your name (again): ")
    if(name == 'Arin'): print("Welcome,Arin Ahmed!\nHope, your day will be good enough")
    else: print("Tumsein na ho payga beta, chor do tum..!")    
elif(name == 'Arin' and pas != 2580):
    print("Your password is incorrect, please try again")
    pas = int(input("Enter your password in integers (again):"))
    if(pas == 2580): print("Welcome,Arin Ahmed!\nHope, your day will be good enough")
    else: print("Tumsein na ho payga beta, chor do tum..!")    
else:
    print("Your name and password both are incorrect, please try again")
    name = input("Enter your name: ")
    pas = int(input("Enter your password in integers: "))
    if(name == 'Arin' and pas == 2580): print("Welcome,Arin Ahmed!\nHope, your day will be good enough")
    elif(name != 'Arin' and pas == 2580):
        print("Your name is incorrect, please try again")
        name = input("Enter your name (again): ")
        if(name == 'Arin'): print("Welcome,Arin Ahmed!\nHope, your day will be good enough")
        else: print("Tumsein na ho payga beta, chor do tum..!")    
    elif(name == 'Arin' and pas != 2580):
        print("Your password is incorrect, please try again")
        pas = int(input("Enter your password in integers (again):"))
        if(pas == 2580): print("Welcome,Arin Ahmed!\nHope, your day will be good enough")
        else: print("Tumsein na ho payga beta, chor do tum..!")    
    else: print("Tumsein na ho payga beta, dub maro tum..!")    
