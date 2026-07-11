# str1 = "vishal" 
# len1 = len(str1)

# print(len1)

# str2 = "kumar"
# print(len(str2))

# print(str1 + str2)

# str = "vishal_kumar"
# str[0]
# print(str[9])
# print(str[8:])
# print(str[-5:-1])

# print(str.endswith("ar"))

# print(str.capitalize())

# str = "i am studying python with youtub"

# print(str.replace("studying", "learing"))

# print(str.find("w"))

# print(str.count("t"))

# # pratice question
# name = input("enter your name")
# print("lengthn of your name is", len(name))

# str = "hii, $iam the $ symbol $99.99"
# print(str.count("$"))


# if-elif-else(syntax)
# age = 15

# if(age >= 18):
#     print("can vote")
# if(age >= 21):
#     print("can vote")    

# elif(age >= 18):
#     print("CANNOT vote")

# light = "pink"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#      print("look")

# else:
#     print("light is broken")

# pratice question
# marks = int(input("enter student marks : "))


# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student ->", grade)

# PRATICE QUESTION  1.

# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("running")
# elif(light == "green"):
#     print("start")
# else:
#     print("light is not avilable")

# #   NESTING
# age = int(input("enter age number:"))

# if(age >= 18):
#     if(age >= 80):
#         print("cannot dirve")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

#     # PRACTICE QUESTION  2.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if(a >= b and a >= c):
#     print("first number is largest")
# elif(b >= c):
#     print("second number is largest")
# else:
#     print("third number is largest")
    
    #    PRACTICE QUESTION  3.

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
d = int(input("enter the forth numer: "))

if(a >= b and a >= c and a >= d ):
    print("first number is largest")
elif(b >= c and b >= d ):
    print("second number is largest")
elif(c >= d ):
    print("third numwer is largest")
else:
    print("forth numer is largest")
    