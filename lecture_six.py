#   FUNCTION IN PYTHON
def cacl_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cacl_sum(5, 9)
cacl_sum(10, 23)
cacl_sum(55, 65)


def cacl_sum(a, b):
    return a+b

sum = cacl_sum(550, 685)
print(sum)

def print_hello():
    print('hello')

print("hello")   

output = print_hello()
print(output)

#  AVERAGE OF 3 NUMBERS

def cacl_avg(a, b, c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

cacl_avg(15, 21, 10)

#  DEFAULT PARAMETERS
def cacl_prod(a=2, b=5):
    print(a * b)
    return(a * b) 

cacl_prod()

#  PRACTICE QUESTION
# 1. WAF TO  PRINT THE LENGTH OF A LIST.(LIST IS THE PARAMETER)
cities = ["bagaha", "bettiah", "patna", "kanpur", "ghorakhpur", "delhi" ]
vegitables = ["brinjal", "potato", "tomato", "ladyfinger", "onion" ]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(vegitables)    


# 2.WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.(LIST IS THE PARAMETER)
cities = ["bagaha", "bettiah", "patna", "kanpur", "ghorakhpur", "delhi" ]

def print_list(list):
    for item in list:
        print(item, end=" " )

print_list(cities)        

# 3. WAF TO FIND FACTORIAL OF n.(n IS THE PARAMETER)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)

# WAF TO CONVERT USD TO INR.

def converter(usd_val):
    inr_val = usd_val * 97
    print(usd_val, "USD =", inr_val, "INR")

converter(1)

