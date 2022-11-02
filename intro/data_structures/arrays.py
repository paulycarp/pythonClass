# Arrays
# Arrays take less memory and are faster
# If you have large data, replace list with array

from array import array
import numbers

numbers = array("i", [2, 4, 6, 8])

numbers.append(10)
numbers.pop()
numbers.remove(5)
if(7 in numbers):
    numbers.index(7)
