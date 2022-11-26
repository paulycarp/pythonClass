# class Point:
#     x = 2
#     y = 3
#     def read():
#         print("Reading values")

class Point:
    
    def __init__(self, i, j, k):
        self.x = i
        self.y = j
        self.z = k
        self.default_color = "red"

        def draw(self):
            print(f"Point ({self.x}, {self.y}, {self.z})")

point =  Point(9, 3, 18)

print(type(point))
print(isinstance(point, Point))

# point.y = 13
# point.z = -8
print(point.x, point.y, point.z)
print(point.draw())

# Class and instance Attributes
point.j = 21
anotherPoint = Point(9, 7, 3)
print(point.j)
print(anotherPoint.draw(), anotherPoint.defaul_color)

# Class vs Instance Methods
point = Point(0, 0, 0)
print(point.draw())
# print(point.zero())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def zero(cl):
        return cl(0, 0)

    def __str__(self) -> str:
        return(f"({self.x}, {self.y})")
    
    def __eq__(self, __o: object) -> bool:
        return self.x ==__o.x and self.y == __o.y # comparint Object
    
    def __gt__(self, __o:object) -> bool:
        return self.x > __o.x and self.y > __o.y

    def __add__(self, __o:object) -> object:
        return Point(self.x + __o.x and self.y + __o.y)

point = Point(2, 4)
print(point.zero().x)

#  Magic Method (__magic__())
print(str(point))

# comparing Objects
point = Point(1, 2)
other = Point(1, 2)
point2 = Point(3, -4)

print(point == other)
print(point > point2)