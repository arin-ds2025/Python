class Student:
    
    def __init__(self,name,roll,cgpa): # this is a constructor, using __init__
        self.n = name # it means, create an instance attribute of n and assign it with n
        self.r = roll # same goes for r
        self.cg = cgpa # same goes for cg
        
    def get_info(self):
        print(f"Hey {self.n},\nRoll: {self.r}\nCGPA: {self.cg}")
        print(" ")
        
s1 = Student("Arin",758572,3.57) # in case of using constructor, we've instant pass arguments while creating object
s1.get_info()

s2 = Student("Nayem",758578,3.23) # same
s2.get_info()