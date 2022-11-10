# Tuples are immutable
# Readonly list
#from re import A


point = (1, 2)
print(type(point))
# if we exclude paranthesis, we still have a tuple
point = 1, 2
print(type(point))

point = ()
point = (1,)
print(point[0])

# Concateneate
point = (1, 2) + (3, 4)
print(point)

# Repeat
point = (1, 3) * 5
print(point)


# Convert list to tuple
point = tuple([1, 2, 3, 4, 5,])
print(point)
point = tuple("books")
print(point)
print(point[:2])
print(point)

# Unpack
x, y, *z= point
print(x)
print(y)
print(z)

# "in" keyword

# loop
for val in point:
    print(val)

# We cannot mutate
point

# swaping variables

a = 5
b = 8

# solution

temp = b
b = a
a = temp

print(a, b)

x = 2
y = 7

x, y = y,  x

print(x,y)