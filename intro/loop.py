"""use loops to avoid repetition"""
# for loops
# rang syntax => range()


for number in range(10):
    print("TAACODEEP", number)

TAACODEEP = "The best coding school you can ever attend"

for num in range(1, len(TAACODEEP), 2):
    print(num)
for letters in TAACODEEP:
    print(letters)

# count backwards
for num in range(100, 0, -10):
    print(num)

# to print triangle
for triange in range(8):
    print((triange + 1) * "* ")

# for/else
SUCCESS = True
for num in range(3):
    print("Attempt..")
    if SUCCESS:
        print("Successful")
        break
else:
    print("Attempted 3 times and fialed")

# Nested loop
for x in range(8):
    for y in range(5):
        print(f"({x}, {y})")

# while loops
NUM = 300
while NUM > 0:
    print(NUM)
    num //= 2 #interger division, it doesn't return decimal places

COMMAND = ""
while COMMAND.lower() != "end":
    COMMAND = input(">")
    print("Say", COMMAND)

#INFINITE LOOP
while True:
    print("OK")
    break#this helps to breake the loop, else it will continue till infinity
