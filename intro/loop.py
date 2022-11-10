"""use loops to avoid repetition"""
# for loops
# rang syntax => range()


for number in range(10):
    print("taacodeep", number)

taacodeep = "The best coding school you can ever attend"

for num in range(1, len(taacodeep), 2):
    print(num)
for letters in taacodeep:
    print(letters)

# count backwards
for num in range(100, 0, -10):
    print(num)

# to print triangle
for triange in range(8):
    print((triange + 1) * " *")

# for/else
success = True
for num in range(3):
    print("Attempt..")
    if success:
        print("Successful")
        break
else:
    print("Attempted 3 times and fialed")

# Nested loop
for x in range(8):
    for y in range(5):
        print(f"({x}, {y})")

# while loops
num = 300
while num > 0:
    print(num)
    num //= 2 #interger division, it doesn't return decimal places

command = ""
while command.lower() != "end":
    command = input(">")
    print("Say", command)

#INFINITE LOOP

while True:
    print("OK")
    break#this helps to breake the loop, else it will continue till infinity
