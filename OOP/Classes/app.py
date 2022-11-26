# class Point:
#     x = 2
#     y = 3
#     def read():
#         print("Reading values")

class Point:
    def __init__(self, i, j, k):
        self.x = i
        self.x = j
        self.x = k

point =  Point(9, 3, 18)

print(type(point))
print(isinstance(point, Point))

# point.y = 13
# point.z = -8
print(point.x, point.y, point.z)
print(str(point))