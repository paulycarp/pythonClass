"""Functions and Functional Programming"""
import math


def fullname(first_name, last_name):
    """Any Dommy string"""
    print(f"{first_name} {last_name}")

# Return a value
def uppercase(word):
    """Any Dommy string"""
    return word.upper()

def fizzbuzz():
    """any Dommy string"""
    print("Fissbuss challenge")

print(uppercase("lottry"))

# Volume of cylinder
def cylindervol(radius, height):
    _pie = math.pi
    return _pie * math.pow(radius, 2) * height

print(cylindervol(5, 5))

# Keyword Arguments
def increment(num, _by):
    return num + _by

RESULT = increment(2, 1)
print(RESULT)

# Default Arguments
# All optional parameters should come aftr the required parameter
def incrementeasy(num, _by=1):
    """Any Dommy string"""
    return num + _by

VALUE1 = incrementeasy(5)
VALUE2 = incrementeasy(5, 19)
print(VALUE1)
print(VALUE2)

# REST PARAMETERS
def multiply(_x,_y):
    """Any Dommy string"""
    return _x * _y

print(multiply(7, 2))

# To be able to the issue of mutiple required parameters we do the following

def multiply_more(*numbers):
    """Any Dommy string"""
    return numbers

print(multiply_more(4, 3, 6, 9, 1, 4))

def multi(*numb):
    """Any Dommy string"""
    total = 1
    for num in numb:
        total *= num
    return total
print(multi(3, 5, 7, 8, 2))

# working with dictionary
def save_user(**user):
    """Any Dommy string"""
    print(user)

save_user(id = 1, name = "Paullycarp", age = 34)

# SCOPE
# A region where a piece of code is defind

def volume(radius):
    height = int(input("height: >"))
    return math.pi * radius * radius * height

print(volume(7))

message = "messeage a"

def greet(name):
    message = f"messag {name}"
    return message

print(greet("John"))

