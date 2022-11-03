"""If you want to print FizzBuss do the following"""
def fizz_buzz(ouput):
    """Any dummy string."""
    if ouput % 15 == 0:
        return "FizzBuzz"
    if ouput % 3 == 0:
        return "Fizz"
    if ouput % 5 == 0:
        return "Buzz"
    return ouput

print(fizz_buzz(45))

FIZZ_BUZZ = (input)
if input % 15 == 0:
    print("Fizzbuss")
elif input % 3 == 0:
    print("Fizz")
elif input % 5 ==  0:
    print("Buzz")
else:
    print(input)



DIGITS = list(range(100))
print(DIGITS[::2])

for num in range(1, 100, 2):
    add = num + 1
    print(add)
