import sys
import pickle

class Person:
    def __init__(self, name) -> None:
        self.name = name
    def setAge(self, age):
        self.age = age


david = Person("David")
david.setAge(29)

try:
    d = open("object.bin", "wb")
except:
    print("Failure in opening file.")
    sys.exit(0)

pickle.dump(david, d)

d.close()
david = None

try:
    d2 = open("object.bin", "rb")
except:
    print("Failure in opening file.")
    sys.exit(0)

x = pickle.load(d2)
print(x)

d2.close()