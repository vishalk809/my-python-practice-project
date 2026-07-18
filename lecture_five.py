#  LOOPS
#    WHILE LOOPS
count = 1
while count <= 5:
    print("hello")
    count += 1

i = 1
while i <= 10:
    print("vishalkumar", i)
    i+=1

#  PRACTICE QUESTION
#  1.PRINT NUMBERS FROM 1 TO 100.
i = 1
while i <= 100:
    print(i)
    i += 1

# 2. PRINT NUMBERS FROM 100 TO 1.
i = 100
while i >= 1:
    print(i)
    i -= 1

# 3. print the multiplication table of a number n.
i = 1
# n = int(input("enter the numer: "))
while i <= 10:
    print(15*i)
    i += 1

# 4. PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# 5. SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 81

i = 0
while i < len(nums):
    if(nums[i] ==x):
        print("FOUND at idx" , i)
    i += 1

#         KEYWORDS
#  BREAKE
i = 1 
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")
 
#   CONTINUE

i = 0 
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

#  FOR LOOPS
nums = [1, 2, 3, 4, 5, 6]

for val in nums:
    print(val)


tup = (1, 2, 3, 4, 5 )

for num in tup:
    print(num)

str = "apnacollage"

for char in str:
    print(char)

    #  ELSE
    str = " vishalkumar"

    for char in str:
        print(char)
    else:
        print("END")

#  PRACTICE QUESTION
# SEARCH FOR A  NUMBER X IN THIS TUPLE USING LOOP:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, )
x = 16

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1

