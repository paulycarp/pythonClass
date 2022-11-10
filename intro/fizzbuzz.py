"""If you want to print FizzBuss do the following"""
def fizz_buzz(ouput):
    if ouput % 15 == 0:
        return "FizzBuzz"
    if ouput % 3 == 0:
        return "Fizz"
    if ouput % 5 == 0:
        return "Buzz"
    return ouput

print(fizz_buzz(5))

def Fizz_Buzz(input):
    if input % 15 == 0:
        print("Fizzbuss")
    elif input % 3 == 0:
        print("Fizz")
    elif input % 5 ==  0:
        print("Buzz")
    else:
        print(input)

print(Fizz_Buzz(45))

print("\n******** Working with range in for loop ********\n")
digits = list(range(100))
print(digits[::2])

for num in range(1, 100, 2):
    add = num + 1
    print(add)
