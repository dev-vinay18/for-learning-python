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

class account :
    def __init__( self, acc_no, acc_pass ):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = account(23456 , "acgx")
acc1.acc_no
print(acc1.acc_no)