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
point(point)

# Add New value
point["k"] = 23
print(point)

# Looking for value that does not exixt, it give a "keyError"
#print(point["a"])

# we need to check if the key exists if we are not sure

if "a" in point:
    print(point["a"])

