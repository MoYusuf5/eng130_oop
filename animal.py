# create a class called Animal - file-name start with a - class name starts with A
# add the common attributes/var behaviours/functions
# syntax `class name: - class Animal:`

class Animal: # follow the correct naming convention & best practices
    # we need to initialise it with a built-in method called __init__(self)
    # self refers to current class
    def __init__(self): # any attributes attached to the class should be part of the init method
        # self.var = True
        self.alive = True
        self.spine = True
        self.eyes = True

# let's create some methods to add common behaviours
    def breathe(self):
        return "keep breathing to stay alive"
    def eat(self):
        return "time to eat!"

# create an object of this class
cat = Animal() # creating an object of this animal class
# print(cat.breathe()) # calling a method using an object of the Animal class
# print(cat.eat())
