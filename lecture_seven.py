# FILE I/O ( INPUT / OUTPUT)

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
 
#  READING A FILE

f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()
 
#  WRITING TO A FILE

f = open("demo.txt", "w")

f.write("i want to learn javascript")

f.close()

# /////////
f = open("demo.txt", "a")

f.write("\n I love javascript")

f.close()

#  WITH SYNTAX
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

# with open("demo.txt", "w") as f:
#     f.write("\n new data")    

#  DELETING A FILE
# import os

# os.remove("file name")

# PRACTICE QUESTION  //////////////////
# 1.CREATE A NEW FILE "PRACTICE.TXT" USING PYTHON. ADD THE FOLLOWING DATA IN IT:

with open("practice.txt", "w") as f:
    f.write("hi everyone\n we are learning file I/O\n")
    f.write("using java.\n i like programming in java.")

# 2. WAF THAT REPLACES ALL OCCURENCES OF "JAVA" WITH "PYTHON" IN ABOVE FILE.
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)    

with open("practice.txt", "w") as f:
    f.write(new_data)

# SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT.
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")   

check_for_word()

# 4.WAF TO FIND IN THE WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FKRST. PRINT -1 IF WORD NOT FOUND
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open ("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()
 
# FROM A FILE CONTAINING NUMBERS SEPARATED BY COMMA,  PRINT THE COUNT OF EVEN NUMBER.
count = 0 
with open("sample.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count += 1

print(count)
