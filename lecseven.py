###### File I/O in python #####
f = open("demo.txt","r")

# print(type(data))

# data = f.read()                     # for reading entire file.
# print(data)

line1 = f.readline()                 # read 1 linwe at 1 time.
print(line1)

line2 = f.readline()
print(line2)

f.close()