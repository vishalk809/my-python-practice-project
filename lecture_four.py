#  DICTIONARY IN PYTHON
info = {
    "name" : "vishal kumar",
    "class" : "P.G",
    "sabject" : ["pyhon", " java", "c", "c++"],
    "age" : 21
    
}

info["name"] = "vikash ,kumar"              

print(info)
print(type(info))
print(info["name"])
print(info["class"])
print(info["sabject"])

#  EMPUTY DICTIONARY
null_dict = {}

null_dict["name"] = "dhiraj kumar"
null_dict["age"] = 21

print(null_dict)

#  NESTED DICTIONARY
student = {
    "name " : "vishal kumar",
    "subject" : {
        "maths" : 94,
        "science" : 80,
        "hindi" : 85
    } 
}
print(student)
print(student["subject"])
print(student["subject"]["maths"])

#  METHODS
print(student.keys())     
print(len(student))
print(list(student))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))
paris = list(student.items())
print(paris[0])

print(student.get("name"))

student.update({"city" : "bagaha"})
print(student)

# SET IN PYTHON
collection = {1, 2, 3, 4, "hellow", "world"}

print(collection)
print(type(collection))

#  EMNPUTY SET SYNTAX
collection = set()
print(type(collection))

# SET METHODS 
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
# 
collection.remove(3)

print(collection)
# 
collection2 = {"hello", "world","python", "java Script","apna colage"}

print(collection2.pop())
# 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
 
print(set1.union(set2))
print(set1)
print(set2)
# 
print(set1.intersection(set2))

#  PRACTICE QUESTIONS //
#   STORE FOLLOWING WORDS MEANINGS IN A PYTHON DICTONARY :
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dictionary)

# YOU ARE A GIVEN A LIST OF SUBJECTS FOR STUDENTS. ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT. 
# HOEW MANY CLASSROOMS ARE NEEDED BY ALL STUDENTS.

subject = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}

print(subject)
print(len(subject))
