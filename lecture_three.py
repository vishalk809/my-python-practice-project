#  LISTS
# marks = [24.5, 88.5, 69.6, 45.2, 74.8]
# print(marks)
# print(len(marks))
# print(type(marks))
# print(marks[0])
# print(marks[1])


# student = ["vishal", 78.6, 21, "bagaha"]
# print(student)
# # //////////
# print(student[0])
# student[0] = "vikash"
# print(student)

# #  LISTS SLICING

# marks = [87, 85, 35, 65, 95]
# print(marks[4])
# print(marks[1:4])
# print(marks[:3])
# print(marks[1:])
# print(marks[-4:-1])

# LISTS METHODS

# list = [2, 1, 3]

# list.append(4)

# list.sort()

#  list.sort(reverse=True)

#  list.reverse()

# list.insert(1, 5)

#  list.remove(1)

# list.pop(2)

# print(list)


#   TUPLES IN PYTHON

tup = (2, 1, 3, 1)

print(tup[0])
print(tup[1])
print(type(tup))
print(tup)

tup = ()
print(tup)
print(type(tup))

tup = (1)
print(type(tup))

tup = (1,)
print(type(tup))

#  TUPLE METHODS
tup = (2, 1, 3, 1)
print(tup.index(3))

print(tup.count(1))

#  PRACTICE QUESTION
#  1. WAP TO ASK THE USER TO ENTER NAMES OF THEIR  FAVORITE MOVIES & STORE THEM IN A LIST.

movies = []

movies1 = input("enter the 1st movies name: ")
movies2 = input("enter the 2nd movies name: ")
movies3 = input("enter the 3rd movies name: ")
movies.append(movies1)
movies.append(movies2)
movies.append(movies3)

print(movies)

# 2. WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.(HINT: USE COPY() ,METHOD)

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindorme")   

    