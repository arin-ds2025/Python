class Point:
    def __init__(self,num1,num2):
        self.x = num1
        self.y = num2
        
    def sum(self,p): # without opertator overloading
        return Point((self.x + p.x) , (self.y + p.y)) 
        
    def __add__(self,q): # for operator overloading
        return Point((self.x + q.x) , (self.y + q.y)) 
        
    def print_text(self): 
        print(f"After sum, self.x is {self.x} and self.y is {self.y}")
        
        
p1 = Point(2,4)
p2 = Point(1,3)

s1 = p1.sum(p2) # it'll return a new Point which is sum of p1 and p2
s1.print_text()
print(" ")


# Operator overloading
q1 = Point(5,6)
q2 = Point(2,8)

s2 = q1 + q2 # it'll also return a new Point which is sum of p1 and p2.. for using + operator, we've to use __add__ in class
# here we overloaded '+' operator by writing __add__ function 
s2.print_text()