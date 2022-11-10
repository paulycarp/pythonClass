# Exceptions are errors that terminates the program
# numbers = [1, 2]
# print(numbers[3])

try: 
    age = input("age: ")
except ValueError:
    print("Not a Valid Age")
else:
    print("No exception thrown")
print("Execution Continues")
for char in "hello":
    print(char)

# number = int(input("No: "))
# print(number)
# for char in "hello":
#    print(char)

# using alias
try:
    age = int(input("Age "))
except ValueError as error:
    print("Not a valid age")
    print(error)
    print(type(error))

try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Age is invalid")
else:
    print("Valid age")