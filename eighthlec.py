## FOR "OOP"(OBJECT ORIENTED PROGRAMMING) PROGRAMMING. ##
## to map with real world scenarios , we are started using objects in code.
## this is called object oriented programming.

## class and object in python.
## class is blueprint for creating objects.

# class student:
#     name = "arnav"

# s1 = student()
# print(s1.name)

# s2 = student()
# print(s2.name)

# class car:
#     color = "yellow"
#     brand = "bmw"

# c1 = car()
# print(c1.color)
# print(c1.brand)

## (__init__) Function
## constructor = object creation 
## All classes have function _init_(), which is always executed when the object is being intiated.

class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
        print("This function is added now..")

N1 = student("tejas", 20)
print(N1.name)
print(N1.marks)
        