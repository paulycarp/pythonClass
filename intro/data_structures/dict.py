# Dictionaries
# Dictionaries are like objects in JS. They are key-value paired representation
# of value

point = { "x": 1, "y": 3}

# You can only use immutation values as key

# Creating dictionaries with the constructor

point1 = dict(x = 5, y = 8, z = -1)
print(point1)

# Access
z_axis = 'z'
print(point["y"])
print(point1[z_axis])

# Update (Let us update x to 12)
point["x"] = 12
print(point)

# Add New value
point["k"] = 23
print(point)

# Looking for value that does not exixt, it give a "keyError"
#print(point["a"])

# we need to check if the key exists if we are not sure

if "a" in point:
    print(point["a"])

# OR
print(point.get("a"))
print(point.get("a", 0))

# To delete
del point["k"]
print(point)

# Looping
print(point1)
for x in point1:
    print(x)

# Print key and value
for key in point1:
    print(key, point1[key])

# OR
for x in point1.items():
    print(x)

# unpacking
for key, value in point1.items():
    print(key, value)

# Dictionary Comprehension
# Recall
value = []
for x in range(6):
    value.append(x * 2)

# List comprehension [expression for item in items]

value = [x * 2 for x in range(5)]

# If we replace the squre bracket with curly braces, we get a set

value = { x * 2 for x in range(6)}
print(value, type(value))

# To create dictionary comprehension
value = {x: x * 2 for x in range(6)}
print(value)

# Generator Expression
value = (x * 2 for x in range(20))
print(value)

from sys import getsizeof

values0 = [x * 2 for x in range(15000)]
print("list", getsizeof(values0))

values1 = ( x * 2 for x in range(15000))
print("gen", getsizeof(values1))

#number0

val = [*range(5), *"Schools"]
print(val)

# Combining lists
first = [1, 2]
second = [3]
vals = [*first, "a", *second, *"Hello"]
print(vals)

# Unpack dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}

combined = {**first, **second, "z": 1}
print(combined)

# Given:
# sentence = "This is a common interview question, you can try it out."
# find the most repeated character in a text (spaces not included)