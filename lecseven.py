###### File I/O in python #####
## "r" = for reading a file (default,if dont write any other function thin read is defaultly selected.)
 
# f = open("demo.txt","r")

# print(type(data))

# data = f.read()                     # for reading entire file.
# print(data)

# data = f.read(9)                       # we can also pass an argument(index value) for our need.
# print(data)

# line1 = f.readline()                 # read 1 linwe at 1 time.
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

## "w" = for writing to a file

f = open("demo.txt","w")

f.write("new")

## "a" = for adding 