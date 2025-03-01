# info= {
#     "name" : "vinay",
#     "age" : 20,
#     "subjects" : ["python", "java", "c++" ],
#     12.96 : 23.45
# }
# print(info["name"])
# print(info["age"])

# info= {
#     "name" : "vinay",                                            # from this we can say that dictionary in python are mutable
#     "age" : 20,
#     "subjects" : ["python", "java", "c++" ],
#     12.96 : 23.45
# }

# info["name"] = "arnav"
# info["surname"] = "wattamwar"

# print(info) 

# dict_info = {}                                                     # we can create null dictionary and add 
# dict_info["name"] = "vinay"
# print((dict_info))

# student = {                                                          # nexted dictionary 
#     "name" : "arnav gore",
#     "subject" : {
#         "physics" : 80,
#         "chemistry" : 90,
#         "mathematics" : 95 
#     }
# }

# print(student["subject"]["chemistry"])


# student = {                                                          # for getting key pts. (but don't show nested key pts.)     
#     "name" : "arnav gore",
#     "subject" : {
#         "physics" : 80,
#         "chemistry" : 90,
#         "mathematics" : 95 
#     }
# }

# print(len(student))                                   
# print(list(student.keys()))                                        # student.keys() it returns all keys.
# print(list(student.values()))                                      # student.values() it returns all value ( nest values also .) 
# pairs = list(student.items())                                      # pairs function it gives pairs of that row ( for pair we use '[]' bracket.)
# print(pairs[0])
# print(list(student.items()))                                       # in this we gate the values in tuple.

# print(student.get("name"))                                         # if we use .get then we don't gate any error and it just gives none .
# print(student["name"])                                             # it gives error if the key is wrong thats why in coding we should prefer to write '.get' first.

# student.update({"city" : "pune"})
# print(student)

# new_dict = ({"city" : "pune"})                                       # for creating a new dict. (dict. dont allow  dublicate keys.)
# student.update(new_dict)              
# print(student)

# print(type(student))

####################################### SET ##############################################

# collection = { 1, 2,2,2, 3 , "hello","hello","world"}                       # in this set every dublicate value is ignored.           
# print(collection)
# print(type(collection))

# collection1 = set()                                                     # for empty set. 

# collection2 = set()        
# collection2.add(1)                                                       # .add for adding values in set.
# collection2.add(2)
# collection2.add(2)
# collection2.add("my")
# collection2.add("college")
# collection2.remove(1)                                                    # .remove for removing values in the set.

# collection2.clear()                                                      # .clear for empty the whole set. 
# print(collection2)  
# print(len(collection2))

# set = {2,3,4}
# set0 = {3,4,5}
# print(set.union(set0))                                                     # .union it show all the values of both the set but dont show repeted values.
# print(set)
# print(set.intersection(set0))                                                # .intersection show the similar values of both sets.

################## PRACTICE QUESTIONS #######################


# dict3 = {
#     "table" : ["a piece of furniture" , "list of fact and figures"],          # 1st Q
#      "cat" : "a small animal"
# }
# print(dict3)

# subjects = {"python","java","python","java","c++"                               # 2nd Q
#          "c","java","c","c++"}
# print(len(subjects))

# marks = {}                                                                     # 3rd Q

# x = int(input("enter phy :"))
# marks.update({"phy" : x})

# x = int(input("enter chem :"))
# marks.update({"chem " : x})

# x = int(input("enter math :"))
# marks.update({"math" : x})

# print(marks)

values = {9,"9.0"}
     # OR #
values1 = {
    ("float",9.0),
    ("int",9)
}

print(values)
print(values1)