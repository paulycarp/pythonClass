# Lists

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
num = [[1, 4], [2, 8]]
twos = [2] * 9 # This line will help us to repeat content of a list

print(twos, num)
print(type(num))

# Concatination
alphanum = letters + twos # This line of code helps us to concatinate two lists
print(alphanum)

numbers = range(10)
print(list(numbers))
print(list('classified'))

# Lenght
len(alphanum)

# Accessing List
# We use [] to access list

alphanum[5]

# slice

print(alphanum[1:4])
print(alphanum[::4])
print(alphanum[1::5])

nums = range(40)

print(list(nums[::2])) # Lists range of numbers in step of 2 (even numbers)
print(list(nums[::-1])) # Lists range of numbers in step of -1 ()
print((nums[::-1]))
print((nums[::3])) # Lists range of numbers in step of 2 (even numbers) without listing them explicitly

# unpacking list

number1 = [1, 2, 3]
frist = number1[0]
second = number1[1]
third = number1[2]

number2 = [1, 2, 3,]
first, second, third = number2

number3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
first, second, third, *other = number2

# Looping
for letter in letters:
    print(letters)

for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

# Adding and Removing items into and from a list

letter1 = ["a", "b", "c", "f", "g"]
#Add
letter1.append("d")
print(letter1)
letter1.insert(0, "_")
print(letter1)

# Remove
letter1.pop()
letter1.pop(1)
print(letter1)

# When you don't know the index
# We use
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

letter2 = ["a", "b", "c", "e", "f", "g", "f"]
#print(letter2.index("h"))
print(letter2.index("b"))

if "d" in letter2:
    print(letter2.index('d'))

# number of occurrence (telling us the number of occurrence of a letter)
print(letter2.count('f'))

# Sorting List
num = [3, 1, 7, 0, 2, 8, 5, 9, 6, 4]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

num = [3, 1, 7, 0, 2, 8, 5, 9, 6, 4]
numSorted = sorted(num)
print(numSorted)

#Complex Sorting
item = [
    ("Produce1", 45),
    ("Produce2", 15),
    ("Produce3", 10),
]

item.sort()
print()
