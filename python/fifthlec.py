########################## LOOPS ##############################
########## while loop #############

# count = 1                                                 # in loops they repeat instructions. (thats why we use condition after 'while')
# while count <= 5 :                                        # and this repeating called as Iteration.
#     print("arnav")
#     count += 1 

# i = 1
# while i <= 5 :
#     print("gore")
#     i += 1

# j = 1                                                       # print numbers from 1 to 5. Q
# while j <= 5 :
#     print(j)
#     j += 1

# print("loop ended")

# k = 5                                                       # print numbers from 5 to 1. Q
# while k >= 1 :
#     print(k)
#     k -= 1

# print("loop ended.")

# m = 1                                                         # print numbers from 1 to 100. Q
# while m <= 100 :
#     print(m)
#     m += 1

# n = 100                                                      # print numbers from 100 to 1. Q
# while n >= 1 :
#     print(n)
#     n -= 1   

# n = int(input("enter value : "))                                 # print the multiplication number of n. Q
# y = 1
# while y <= 10 :
#     print(n*y)
#     y += 1

# nums = [1,4,9,16,25,36,49,64,81,100]                             #print the elements of the folowing number using loop. Q (traverse means to travel from one to anthoher.)

# idx = 0 
# while idx < len(nums) :
#     print(nums[idx])
#     idx += 1

# nums = (1,4,9,16,25,36,49,64,81,100)                              # this loop is for finding a number in a tuple. Q 

# x = 49
# g = 0

# while g < len(nums) :
#     if(nums[g] == x) :
#         print("found at index", g)
#     else:
#         print("finding...")
#     g += 1

# nums = (1,4,9,16,25,36,49,64,81,100)                             #  use of 'brake' . 

# x = 49
# g = 0

# while g < len(nums) :
#     if(nums[g] == x) :
#         print("found at index", g)
#         break
#     else:
#         print("finding...")
#     g += 1

# d = 1                                                              # 'continue' : it use for skiping

# while d <= 10 :
#     if(d%2 != 0):
#         d += 1
#         continue  # skip
#     print(d)
#     d += 1 

##################### for loop #######################

# str = "apnacollege"                                                 # ex for for loop. 

# for char in str :
#     print(char)
# else:
#     print("END") 

# e = [1,4,9,16,25,36,49,64,81,100]                                    # print the following number while using loop. Q

# for val in e :
#     print(val) 

# a = (1,4,9,16,25,36,49,64,81,100,49)                                 # ex. for for loop               
# x = 49
# idx = 0

# for el in a :                                                       
#     if(el == x):
#         print("number found at idx :", idx)
#     idx += 1

# s = "apnacollege"                                                     # practice Q.

# for char in s :
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)

# print("END") 

############ RANGE ############

## Range function returns a sequence of number starting from 0 by default, and increments by 1 (by default), and stop before a specified number.
## range(start?,stop,step?)

# for i in range(10):                                               # examples 
#     print(i)

# for t in range(1,10): 
#     print(t)

# for f in range(0,10,2):
#     print(f)

###### practice question ######

# for p in range(1,101):                                              # print numbers from 1 to 100.
#     print(p)

# for z in range(100,0,-1):                                          # print numbers from 100 to 1.
    # print(z)

# n =  int(input("enter number :"))                                     # print the multiplication table of no. n

# for c in range(1,11):
#     print(n * c)

# for y in range():                                                    #  'pass' this used for we will complite this later.
#     pass

# n = int(input("enter number :"))                                    # WAP to write the sum of first natural numbers.
# sum = 0

# for i in range(1,n+1):
#     sum += i

# print("sum of n natural number :", sum)

## same q. using while loop

# n = int(input("enter number :"))
# sum = 0 
# i = 1

# while i <= n :
#     sum += i
#     i += 1

# print("print sum :" , sum )

# n = int(input("enter number :"))                                  # WAP to find the factorial of first n number.
# fact = 1

# for g in range(1,1+n) :
#     fact *= g

# print("factorial of number :" , fact )

## same Q. using while 

# n = int(input("enter number :"))
# fact = 1
# s = 1

# while s <= n :
#     fact *= s
#     s += 1

# print("factorial of n :" , fact )
