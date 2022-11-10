print("\n******** working with string ********")
first_name = "Paully"
last_name ="Carp"
age = 34

print("******** working with string concatination ********\n")
full_name = first_name + " " + last_name
greetings = f"My name is: {full_name} I am {age} years old"
print(greetings)
print(full_name.upper())
print(full_name.lower())
print(full_name[5:]) #slizing i.e. getting a part of a string
print(full_name.title()) #this capitalize the first letter

#To trim space i.e. to clear empty spacies
print("\n******** working with trim ********\n")
course = "  Python tutorial   "
print(course.lstrip())
print(course.rstrip())
print(course.strip())

#Get index of string
print("\n******** working with index in string ********\n")
print(course.strip().find("o"))
print(course.strip().find("a"))

#to replace a word in a string
print("\n******** working with word replace in string ********\n")
print(course.replace("tutorial", "Class"))

#to check for existing word in a string
print("\n******** checking for existence of word in string ********\n")
print("python" in course)
print("code" not in course)
