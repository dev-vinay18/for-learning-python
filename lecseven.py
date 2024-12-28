###### File I/O in python #####
## "r" = for reading a file (default,if dont write any other function thin read is defaultly selected.)
 
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

## "r+" = for over writting means characteres from first started replacing which we will write in write mode.
 
# f = open("demo.txt","r+")

# f.write("abc")

# f.close()


