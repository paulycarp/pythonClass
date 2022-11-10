"""Functions and Functional Programming"""
import math

first_name = "DevMan"
last_name = "Paul"

def fullname(first_name, last_name):
      print(f"My name is {first_name} {last_name}")

print(f"My name is {first_name} {last_name}")

# Return a value
def uppercase(word):
    return word.upper()

def fizzbuzz():
    print("Fissbuss challenge")

print(uppercase("lottry"))

# Volume of cylinder
def cylindervol(radius, height):
    pie = math.pi
    return pie * math.pow(radius, 2) * height

print(cylindervol(5, 5))

# Keyword Arguments
def increment(num, by):
    return num + by

result = increment(2, 1)
print(result)

# Default Arguments
# All optional parameters should come aftr the required parameter
def incrementeasy(num, by=1):
    return num + by

value1 = incrementeasy(5)
value2 = incrementeasy(5, 19)
print(value1)
print(value2)

# REST PARAMETERS
def multiply(x,y):
    return x * y

print(multiply(7, 2))

# To be able to the issue of mutiple required parameters we do the following

def multiply_more(*numbers):
    return numbers

print(multiply_more(4, 3, 6, 9, 1, 4))

def multi(*numb):
    total = 1
    for num in numb:
        total *= num
    return total

print(multi(3, 5, 7, 8, 2))

# working with dictionary
def save_user(**user):
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
    message = f"message {name}"
    return message

print(greet("John"))

