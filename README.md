# Python Object Orientated Programming

## 4 Pillars of OOP

### Methods/Functions

### Modules

### Lib - Packages

### Use case - benefits - examples of built in modules - packages

- Random module is a built-in module of Python which is used to generate random numbers
```python
import random
print(random.random()) # each time the program is run, it generates a random float number
print(random.randint(1,100)) # each time the program is run, it generates a random integer between specified numbers
print(random.randrange(1,100)) # each time the program is run, it generates a random numbers in a range
```
- Math module is a built-in module that you can use for mathematical tasks
```python
from random import *
import math

number = 23.66
# any number - to round the figure up
# number 1.5 or more above to round up to 2
# number 1.49 or less to round down to 1
print(math.ceil(number)) # 'ceil' will help you round the number up
print(math.floor(number)) # 'floor' will help you round the number down
```

