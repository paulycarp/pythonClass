"""formarting strin"""
first_name = "Paully"
last_name ="Carp"
age = 34

full_name = first_name + " " + last_name
greetings = f"My name is: {full_name} i am {age} years old"
print(greetings)
print(full_name.upper())
print(full_name.lower())
print(full_name[5:]) #slizing i.e. getting a part of a string
print(full_name.title())

#To trim space i.e. to clear empty spacies
course = "  Python tutorial   "
print(course.lstrip())
print(course.rstrip())
print(course.strip())

#Get index of string
print(course.strip().find("o"))
print(course.strip().find("s"))

#to replace a word in a string
print(course.replace("tutorial", "Class"))

#to check for existing word in a string
print("python" in course)
print("code" not in course)