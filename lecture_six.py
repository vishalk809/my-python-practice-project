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

