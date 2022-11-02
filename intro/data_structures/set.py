# Sets are used to remove duplicates


import numbers

numbers = [1, 1, 2, 2, 3, 4, 5]
uniques = set(numbers)

print(uniques)

# Creating sets
second = {0, 9, 8, 7, 6}
# Add new item
second.add(5)
print(second)
# Remove
second.remove(8)
# Get lenght
len(second)
print(second)

# mathematical stuffs

first =  set([1, 3, 5, 7])
second = {2, 4}

# Merging (UNION)
print(first | second)

# INTERSECTION
print(first & second)

# DIFFERENCE
print(first - second)

# SYMMETRIC DIFFERENCE
print(first ^ second)

# "in" keyword
# set is unordered

if 1 in first:
    print("yes it is true")

