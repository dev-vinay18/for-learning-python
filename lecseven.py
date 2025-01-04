###### File I/O in python #####
## "r" = for reading a file (default,if we dont write any other functions than read is defaultly selected.)
 
# f = open("demo.txt","r")

# print(type(data))

# data = f.read()                     # for reading entire file.
# print(data)

# data = f.read(9)                       # we can also pass an argument(index value) for our need.
# print(data)

# line1 = f.readline()                 # read 1 line at 1 time.
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

## "w" = for writing to a file                 # in write & append mode if we open any non existed file then thet file will be opened automatically. 

# f = open("demo.txt","w")

# f.write("new")

## "a" = for adding 

# f = open("demo.txt","a")

# f.write("\nwe will learn from tommarow.")

# f.close()

# "r+" = for over writting means characteres from first started replacing which we will write in write mode. (no truncate)
 
# f = open("demo.txt","r+")

# f.write("nw")

# f.close()

## "w+" = when we write in w+ mode then file will be truncated(means file will become empty.) after that we can write any thing using write mode.

# f = open("demo.txt","w+")

# print(f.read())
# f.write("abc")

# f.close()

## "a+" = it will read and append new things. no truncate.

# f = open("demo.txt","a+")

# print(f.read())
# f.write("bcs")

# f.close()

######## With syntax ########
## advantages of using With syntax : we dont want to use close file in ending in with syntax.

# with open ("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open ("demo.txt","w") as f:
#     f.write("new data")

######## impot os #########
## IMP = in this we can deleat any file by rmoving os .

# import os

# os.remove("new.txt")

####### Practice Question ########

## Q1
 
# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning file I/O")
#     f.write("\nUsing java\nI like programming in java.")

# with open ("demo.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java", "python")
# print(new_data)

# with open ("demo.txt","w") as f:
#     f.write(new_data)