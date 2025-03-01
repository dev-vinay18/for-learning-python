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

# class student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks
#         print("This function is added now..")

# N1 = student("tejas", 20)
# print(N1.name)
# print(N1.marks)

# N2 = student("arnav", 38)
# print(N2.name, N2.marks)

# class student:

#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student:", self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = student("arnav" , 35)
# s1.welcome()
# print(s1.get_marks())

## Q

# class student:
#     college_name = "hi-tech institue of tech." #class attribute.

#     def __init__(self,name,marks):
#         self.name = name #object attribute.         (object attribute > class attribute if both have same attribute names)
#         self.marks = marks

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score in list :" , sum/3)

# s1 = student("arnav", [77,67,39])
# s1.avg_marks() 
          
## Important
## 1) abstraction : hiding the implementation detail of a classand only showing the essential features to the user.
## 2) Incapsulation : Wrapping data and functions into a singal unit (object). 
 
## Q

class Account :
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,ammount):
        self.balance -= ammount
        print("RS.", ammount, "is debited..")
        print("total balance =" , self.get_balance() , "Rs.")

    def credit(self,ammount):
        self.balance += ammount
        print("Rs.", ammount, "is credited.. ")
        print("total balance =" , self.get_balance(), "Rs.")

    def get_balance(self):
        return self.balance

acc1 = Account(10000 , 123456)
acc1.debit(200)
acc1.credit(100)

acc2 = Account(20000 , 234567)
acc2.debit(500)
acc2.credit(900)



 