# Lists
print("\n******** Working with List ********\n")

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
num = [[1, 4], [2, 8]]
twos = [2] * 5 # This line will help us to repeat content of a list

print(twos, num)
print(type(num))

# Concatination
print("\n******** Concatinate ********\n")
alphanum = letters + twos # This line of code helps us to concatinate two lists
print(alphanum)

numbers = range(10)
print(list(numbers))
print(list('classified'))

# Lenght
print("\n******** Lenght of a string ********\n")
print(len(alphanum))

# Accessing List
print("\n******** Accessing List item ********\n")
# We use [] to access list

print(alphanum[5])

# slice
print(alphanum[1:4])
print(alphanum[::4])
print(alphanum[1::5])

nums = range(30)

print(list(nums[::2])) # Lists range of numbers in step of 2 (even numbers)
print(list(nums[::-1])) # Lists range of numbers in step of -1 (counting from back)
print((nums[::-1]))# Lists range of numbers in step of -1 (odd numbers) without listing them explicitly
print((nums[::3])) # Lists range of numbers in step of 2 (even numbers) without listing them explicitly

# unpacking list
print("\n******** Lsit unpacking ********\n")
number1 = [1, 2, 3]
frist = number1[0]
second = number1[1]
third = number1[2]

number2 = [1, 2, 3,]
first, second, third = number2

print(first, third)

number3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
first, second, third, *others= number3

print(first, second, others)

# Looping
print("\n******** Working with Loop ********\n")
for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

# Adding and Removing items into and from a list
print("\n******** Adding and Removing item from a list ********\n")

letter1 = ["a", "b", "c", "f", "g"]

#Add
letter1.append("h") # Adds h at the end of the list
print(letter1)
letter1.insert(3, "d") # inserting "h" at index 3
print(letter1)

# Remove
letter1.pop()
letter1.pop(1)
print(letter1)

# When you don't know the index
# We use letters
letter1.remove("c")
print(letter1)

# Using del Statment, we are deleting a particular index
del letter1[0]
print(letter1)

# We can use clear method to clear a list
letter1.clear()
print(letter1)

# Finding Items in a list
# to find index of item
print("\n******** working with finding item in a list ********\n")

letter2 = ["a", "b", "c", "e", "f", "g", "f"]
#print(letter2.index("h"))
print(letter2.index("b"))

if "d" in letter2:
    print(letter2.index('d'))

# number of occurrence 
# telling us the number of occurrence of a letter

print(letter2.count('f'))

# Sorting List
print("\n******** working with sort ********\n")

num = [3, 1, 7, 0, 2, 8, 5, 9, 6, 4]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

num = [3, 1, 7, 0, 2, 8, 5, 9, 6, 4]
numSorted = sorted(num)
print(numSorted)

#Complex Sorting
items = [
    ("Produce1", 15),
    ("Produce2", 45),
    ("Produce3", 10),
]

items.sort()
print()
print(items)

# create a sort function
def sort_item(items):
    return items[1]

items.sort(key=sort_item)
print(items)

items.sort(key=sort_item, reverse=True)
print(items)

# Lambda Functions
print("\n******** Working with Lambda ********\n")
# This is a one line anonymous function we can pass to list method
# items.sort(key=labda parameter: expression) --> basic lambda syntax

items.sort(key=lambda item: item[1])
print(items)

# Map Function
print("\n******** Working with Map ********\n")
items = [
    ("Produce1", 45),
    ("Produce2", 15),
    ("Produce3", 10),
]

prices = []
for item in items:
    prices.append(item)
print(prices)

# Map
prices = list(map(lambda item:item[0], items))
print(prices)

prices = list(map(lambda item:item[1], items))
print(prices)

prices = list(map(lambda item:item * 3, [2, 5, 8, 11]))
print(prices)

# Filter
# Selecting items base on condition
print("\n******** Working with Filter ********\n")

items = [
    ("Produce1", 45),
    ("Produce2", 15),
    ("Produce3", 10),
]

# get all items with price greater than or equal to 10

filtered = []
for item in items:
    if item[1] >= 10:
        filtered.append(item[0])
        #filtered.append(item)
print(filtered)

filtered = list(filter(lambda item:item[1] >= 11, items))
print(filtered)

filtered = list(map(lambda item:item[1], items))
print(filtered)

prices = [items[0] for item in items if item[1] >= 10]
print(filtered)

# List comprehension
print("\n******** Working with List Comprehension ********\n")
# Syntax [expression for item in items]
# Map
prices = list(map(lambda item:item[1], items))
print(prices)

prices = [item[0] for item in items]
print(prices)

# ZIP Function
print("\n******** Working with Zip Comprehension ********\n")
# We use zip to combine two lists into a single list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print(list(zip(list1, list2)))
