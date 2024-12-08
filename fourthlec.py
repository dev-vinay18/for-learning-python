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


student = {                                                          # for getting key pts. (but don't show nested key pts.)     
    "name" : "arnav gore",
    "subject" : {
        "physics" : 80,
        "chemistry" : 90,
        "mathematics" : 95 
    }
}

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
