class Animal: # parent class
    location = "Bangladesh"
    
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    def speak(self): print("Generic animal sound")
    
    
class Dog(Animal): # child class and it inherits from Animal class
    def speak(self):
        print("Dog speaks: Woof")
        

class Cat(Animal): # child class and it also inherits from Animal class
    def speak(self):
        print("Cat speaks: Meaw")
        

# create objects:
my_dog = Dog("Hummer",'Germany')
my_cat = Cat("Maoufi",'Turkish')

# they both have a 'name' attribute (inherited from Animal)
print(my_dog.name)
print(my_cat.name)
print(" ")

# they both have a 'speak' method 
my_cat.speak()
my_dog.speak()
print(" ")

# they both have the parent class attribute
print(my_dog.location)
print(my_cat.location)
print(" ")


'''
    Use case of super() keyword:
    
    Inside a child class, super() let us call methods from the parent class. This is useful when we want to extend the 
    parent's behavior instead of completely replacing it. It's especially important when initializing the parent class's
    part of a child object. 
    
'''

class Bird(Animal):
    def __init__(self, name, breed,color):
        super().__init__(name,breed) # call Animal's __init__ to set 'name' and 'breed' attribute.. we've to pass exactly those arguments here which are exist in Animal constructor
        self.c = color
        
    def speak(self):
        return super().speak() # we also use super() keyword to direct inhert methods of parent class
        
        
my_bird = Bird("Parot",'Amazone','Blue')
print(my_bird.name) # set by Animal's constructor
print(my_bird.breed) # set by Animal's constructor
print(my_bird.c) # set by Bird's constructor