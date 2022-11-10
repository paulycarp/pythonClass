# Stack
# LIFO =  Last In First Out
# We can build with a list

from shelve import Shelf

print("\n******** Working with Stack ********\n")
print("\n******** Working with Shelf ********\n")
shelf = []

# Add
shelf.append("book1")
shelf.append("book2")
shelf.append("book3")

print(Shelf)

#Remove
borrow = shelf.pop() # this will remove book3
print(borrow)

#last item
print(shelf[-1])

if not shelf:
    print("disable")

# using deque library
print("\n******** Working with Deque Library ********\n")
from collections import deque

stack = deque([])

stack.append("bullet")
stack.append("Gun")
stack.append("Gun powder")
stack.append("Shooter")

print(stack)

print(list(stack))
print(list(stack)[2:])

def sum(q, r):
    return q + r

print(5, 4)

# Remove Item
stack.pop()
def removeItem(anyList):
    if not anyList:
        print("empty")
    else:
        print(stack.pop())

removeItem(stack)
print(stack)

