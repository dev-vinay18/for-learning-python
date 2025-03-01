###### Functions & Recursion ########
##  function : block of statements that perform a specific task.

# def cal_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum

# cal_sum(2,4)

# def calc_sum(a,b):  #parameters
#     return a + b

# sum = calc_sum(3,4) #function call ; and values called arguments
# print(sum)

# def p_hello():
#     print("hello")                                               

# p_hello()
# p_hello()
# p_hello()
# p_hello()
# p_hello()                                                         

# output = p_hello()                                                # if function does not give any return value then it will print "None"
# print(output)

## Q. average of 3 numbers

# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg 

# calc_avg(23,34,46)

# print("arnav", end=" ")                                             # 'end=' is use for print different value on same line.
# print("gore")

# def cal_mul(a=1,b=1):                                                # if we dont pass any arguments then we just attach some default values to the a&b given below.(dafault values shoul give at last other whise we will gwt error.)
#     print(a * b)
#     return a * b 

# cal_mul() 

####### practice question ######

# cities = ["delhi", "pune", "mumbai","sambhaji nagar", "baramati"]      # WAP to print length of list   ( list is the parameter.)
# fruits = ["apple","banana","kiwi","pine apple"]

# def p_len (list):
#     print(len(list))
    
# p_len(cities)
# p_len(fruits)

# cities = ["delhi", "pune", "mumbai","sambhaji nagar", "baramati"]      #WAP to print the elements in the list in a single line. ( list is the parameter.)
# fruits = ["apple","banana","kiwi","pine apple"]

# def pri_list (list):
#     for val in list:
#         print(val, end=" ")

# pri_list (cities)
# print()                                                                # give this empty print at last if we getting this '%'  

# def cal_fact(n):                                                     # Q. WAF to find the factorial of n.(n is the parameter)
#     fact = 1
#     for j in range(1,n+1):
#         fact *= j
#     print(fact)

# cal_fact(9)

# def converter(usd_val):                                                # Q. convert inr value to USD.
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val,"INR")

# converter(6)
    
#### home work Question ###

# def function(n):                                                        # is function n is even or odd.
#     if(n % 2 == 0):
#         print(n," is even number")
#     else:
#         print(n, " is odd number")

# function(56)

###################### Recursion ##########################

## recursive function

# def show (n):
#     if(n == 0):          # this is known as " base case " (in given value when n is 0 then it will stop)(we can stop at any value either 0) 
#         return
#     print(n)
#     show(n - 1)

# show(9)

# def fact(n):
#     if( n== 1 or n== 0):
#         return 1
#     return fact(n-1) * n

# print(fact(8))

### Practice question ###

# def calu_sum(n):                # write a recursive function to calculate the sum of first n natural number.
#     if ( n==0 ):
#         return 0
#     return calu_sum(n-1) + n

# print(calu_sum(9))

def print_list(list, idx=0):               # write a recursive function to print all elements in a list. Hint : use list & idx as a parameter.
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango" , "apple", "banana", "litchi"]

print_list(fruits)

