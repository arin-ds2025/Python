date = int(input("Enter number between (1-7): "))

match date:
    case 1: print("This is Saturday")
    case 2: print("This is Sunday")
    case 3: print("This is Monday")
    case 4: print("This is Tuesday")
    case 5: print("This is Wednesday")
    case 6: print("This is Thursday")
    case 7: print("This is Friday")
    case _: # (_) means default, if those cases doesn't match 
        print("Unknown input, try again.!")