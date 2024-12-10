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

s = "apnacollege"

for char in s :
    if(char == 'o'):
        print("o found")
        break
    print(char)

print("END")

