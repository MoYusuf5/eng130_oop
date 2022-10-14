# Object Orientated Programming

### What is OOP?
- Is a method of structuring a program by bundling related properties and behaviours into individual objects


### What Are The 4 Pillars?
- Encapsulation - restricts access to methods and variables
- Abstraction - process of handling complexity by hiding unnecessary information from the user.
- Inheritance - inherit methods from another class 
- Polymorphism - use of common interface for multiple forms (data types)

### What Are The Benefits?
- Reuse of code - DRY (Inheritance)
- Effective problem solving 
- Troubleshooting is easier (Encapsulation)
- Productivity - many libraries available 

### animal.py (Parent Class)
```python
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
```
### reptile.py 
```python
# create a class called Reptile
# how do we make the Animal class a parent class - how could we inherit fom the Animal class

from animal import Animal # importing everything from Animal class
class Reptile(Animal): # inherting from the Animal class
    def __init__(self):
        super().__init__() # super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = True
        self.heart_chambers = [3, 4]

# let's create some methods to add common behaviours
    def hunt(self):
        return "keep working hard to find food!"
    def use_venom(self):
        return "if I have it, I will use it"

smart_reptile = Reptile()
# print(smart_reptile.breathe())
# print(smart_reptile.hunt())
```
### snake.py
```python
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "if I can touch it, I can smell it aswell"

smart_snake = Snake()
print(smart_snake.hunt())
print(smart_snake.use_tongue_to_smell())
print(smart_snake.breathe())
```
