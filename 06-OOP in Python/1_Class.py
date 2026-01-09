class Employee:
    company = "Lenovo"
    
    def set_salary(self,sal):
        self.avg_sal = sal
    
    def get_salary(self,name):
        print(f"Hey {name},\nYour average salaray will be {self.avg_sal}\nFrom {self.company}")
        print(" ")
        
e = Employee() # here, e is an object of the Employee class
e.set_salary(160000)
e.get_salary("Arin")

e.set_salary(130000)
e.get_salary("Shabbir")
print(e.company)