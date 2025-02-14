## del keyword

## Use to delete object properties or object it self. 

# class student :
#     def __init__(self,name):
#         self.name = name

# s1 = student("utkarsh")
# s1.name
# print(s1.name)  
# del s1.name
# print(s1.name)      

## private(like) attributes & methods
## conceptual inplementations in python
## private attributes & methods are meant to be used only within the classand are not accessible from outside the class.

# class account :
#     def __init__( self, acc_no, acc_pass ):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass              ## it only use in similar class.

#     def __init__(self,reset_pass):
#         print(self.___pass)

# acc1 = account(23456 , "acgx")
# acc1.acc_no
# print(acc1.acc_no) 
# print(acc1.__acc_pass) 

## private(like) attributes and methods 
## conceptual inplimentations in python :private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
  
# class person:
#     __name = "anonyous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self. __hello()

# p1 = person()

# print(p1.welcome())

print