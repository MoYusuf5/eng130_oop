# Python Object Orientated Programming

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

## Definition Function
- Don't Repeat Yourself (DRY)
- Reusable - saves time - saves money
- Let's build some functions
- Syntax `def name():`
- Unless the function is called, it will not run anything

```python
# first iteration
def greeting():
    print("Hello Dear") # greet the user
    # keyword called pass
greeting()
```
```python
# greet the user with their name - second iteration
def greet_user(name): # create a function that takes an arg - the name
    print(f"Hello Dear {name}") # adding a string to the user input

greet_user("Mohamed")
```
#### Create a function that takes int as an arg
```python
def add(value1, value2): # take user input as int, then add them together, then display the outcome
    print("This function is to provide additional functionality")
    return value1 + value2 # return statement
# if you are using a return statement and calling the function - it needs to be in a print statement
print(add(2, 2))
```
#### Create a function to *
```python
def multiply(value1, value2): # define function
    return value1 * value2
# take user input
value1 = int(input("Enter a number of your choice"))
value2 = int(input("Enter another number of your choice"))
# call function
print(f"The multiplication of these two number is {multiply(value1, value2)}")
```
#### Create a function to /
```python
def divide(value1, value2): # define function
    return value1 / value2
# take user input
value1 = int(input("Enter a number of your choice"))
value2 = int(input("Enter a number of your choice"))
# call function
print(f"The divison of these two numbers is {divide(value1, value2)}")
```
#### Create a function to %
```python
def modulus(value1, value2): # define function
    return value1 % value2
# take user input
value1 = int(input("Enter a number of your choice"))
value2 = int(input("Enter a number of your choice"))
# call function
print(f"The remainder of these two numbers when divided is {modulus(value1, value2)}")
```
#### Create a function to convert CM to M
```python
def conversion(value1):
    return value1 / 100
value1 = int(input("Enter a number you want to convert to metres"))
print(f"{value1} converted to metres is {conversion((value1))}")
```

## TASKS
```python
# age restriction for movie tickets
# create a condition for 18 & above
# 16 & above
# universal
# pg
# 12a
# 15 & above
# if nothing matched inform the user to enter their age again
# user must not be allowed to enter age over 117 years

print("Please Enter Your Age")
age = int(input())
def movie_rating(age):
    if age >= 18 and age <= 117:
        print("You can watch any movie")
    elif age >= 16 and age < 18:
        print("You can only watch 16 and above movies")
    elif age >= 12 and age < 16:
        print("You can only watch 12a movies")
    elif age >= 8 and age < 12:
        print("You can only watch pg movies")
    else:
        print("Sorry, you cannot watch any movies here")
    return f"Your age is {age}"
print(movie_rating(age))
```

```python
# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

menu = {
    "starters" : ["spring rolls", "Soup", "Salad"],
    "mains" : ["grilled beef", "fried fish"],
    "desserts" : ["apple crumble", "ice cream", "cheesecake"]
}

print("Do You Want To See Our Menu? yes/no: ")
view_menu = str(input())
def ordered(view_menu):
    if view_menu == "yes":
        print(menu)
    elif view_menu == "no":
        return "Thanks, Enjoy Your Day!"

    order_list = []

    order_1 = input("Please make your first order")
    order_list.append(order_1)

    order_2 = input("Please make your second order")
    order_list.append(order_2)

    order_3 = input("Please make your third order")
    order_list.append(order_3)

    return f"Your order is {order_list}"

print(ordered(view_menu))
```

```python
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizzbuzz(n):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif (number % 3 == 0):
        return "Fizz"
    elif (number % 5 ==0):#
        return "Buzz"
    else:
        return number

for number in range(1, 101):
    print(fizzbuzz(number))
```

```python
# create a dictionary student_data
# iterate through the dict
# using control flow - if - elif - else and for loop print all the keys
# print all the values
# print key with matching value

student_data = {
    "name" : "Mohamed",
    "stream" : "DevOps",
    "completed_lessons" : 3,
    "completed_lessons_names" : ["lists", "strings", "loops"]
}
def info_keys(student_data):
    for k in student_data.keys():
        print(k)
        return f"Here is the data... {student_data.keys()}"
def info_values(student_data):
    for v in student_data.values():
        print(v)
        return f"Here is the data... {student_data.values()}"
def info_items(student_data):
    for k, v in student_data.items():
        print(k,v)
        return f"Here is the data... {student_data.items()}"
print(info_keys(student_data))
print(info_values(student_data))
print(info_items(student_data))
```

