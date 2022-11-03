"""control flow"""
#_summary_ comparism operators <, >, >=, <=, ==, !=

print(10 == "10")
print('bag' > 'apple')
print('Bag' > 'BAG')
print(ord("B"))
print(ord("b"))

#COnditional Statements
#if statment
TEMP = 30
if TEMP >= 30:
    print("It's Worm")
    print("Drink water")
print("Done")

#elif
if TEMP > 30:
    print("The weather is geting hot")
    print("let us fill the fridge with bottles of water")

elif TEMP <= 30:
    print("the weather is normalizing")
print("Done")

#else statement
if TEMP > 30:
    print("it is getting hot")
elif TEMP < 30:
    print("It's a good condition")
else:
    print("it's cold")
print("Done")

#Ternary Operator:
AGE = 22
if AGE >= 18:
    print("Eligible")
else:
    print("Not Eligilbe")

if AGE >= 18:
    MESSAGE = "Eligible"
else:
    MESSAGE = "Not Eligilbe"

#Finally we can reduce the further
MESSAGE = "Eligible" if AGE >= 18 else "Not Eligible"
print(MESSAGE)

#Logical operators
#and, or, not
HIGH_INCOME = True
GOOD_CREDIT = True

if HIGH_INCOME and GOOD_CREDIT:
    print("Eligible")
STUDENT = True
if not STUDENT:
    print("Eligible")
else:
    print("Not Eligible")

if (HIGH_INCOME and GOOD_CREDIT) and not STUDENT:
    print("Eligible")
else:
    print("Not Eligible")

#Chaining comparism
#AGE shuld be b/w 18 and 65
if AGE >= 18 and AGE <= 65:
    print("Eligible")

#OR
#much better way 18 <= AGE <= 65
if 18 <= AGE <= 65:
    print("Eligible")
    #QUIZ
#if (10 == "10"):
    print("A")
elif "bag" > "apple" and "base" > "cat":
    print("b")
else: print("c")

print(ord("c"))
