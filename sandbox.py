# learning new skills with CLASSES

class Person:

    def __init__(self, name):
        self.name = name

    def setAge(self, age):
        age = int(age)
        if age < 0 or age > 100:
            age = 0
        self.age = age

    def __str__(self):
        return self.name
    
    def getProp(self):
        return f"{self.name}, {self.age}"
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __sub__(self, other):
        return self.age - other.age
"""
# define name and age of person 1
print()
name = input("Person 1, please enter your name: ")
p1 = Person(name)

age = input(f"{p1} please enter your age: ")
p1.setAge(age)

print("Person 1: ", p1.getProp())
print()

# define name and age of person 2
name = input("Person 2, please enter your name: ")
p2 = Person(name)

age = input(f"{p2} please enter your age: ")
p2.setAge(age)

print("Person 2: ", p2.getProp())
print()

if p1 > p2:
    print(f"{p1} is older than {p2}")
    print(f"{p1} is {p1-p2} years older.\n")
    print(f"Why are you so old {p1}??")
elif p1 == p2:
    print(f"{p1} and {p2} are of same age.")
else:
    print(f"{p2} is older than {p1}")
    print(f"{p2} is {p2-p1} years older.\n")
    print(f"Why are you so old {p2}??")

class task:
    def __init__(self):
        pass
"""

import datetime

past = datetime.date(2022,12,10)
today = datetime.date.today()
delta = today - past
diff = delta.days
print("Diff days: ", diff)


import sandbox2 as sb2

db = sb2.readFile()

print("DB loaded via other program:\n", db)