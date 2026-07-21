#  OOP(OBJECT ORIENTED PROGRAMMING).
class Student:
    name = "vishal kumar"

s1 = Student()
print(s1.name)

# ////////////
class Car:
    name = "scarpio"
    color = "black"

car1 = Car() 
print(car1.color)   

# __INIT__ FUNCTION  ,(CONSTRUCTOR)
class  Student:

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")

s1 = Student("vishal", 94)
print(s1.name, s1.marks)

# CLASS AND INSTANCE ATTRIBUTES
class  Student:
    collage_name = "BBN Collage"

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")

s1 = Student("vishal", 94)
print(s1.name, s1.marks)
print(s1.collage_name)

# METHODS
class  Student:
    collage_name = "BBN Collage"

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("vishal", 94)
s1.welcome()
print(s1.get_marks())

# PRACTICE QUESTION
# 1.create student class that takes name & marks of 3 subjects as argumentsin constructor. then create a method to print the average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii", self.name, "your avg score is:", sum/3)

s1 = Student("vshal kumar", [ 94, 80, 85])
s1.get_avg()

#  STATIC METHODS
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii", self.name, "your avg score is:", sum/3)

s1 = Student("vshal kumar", [ 94, 80, 85])
s1.get_avg()
s1.hello()

# ABSTRACTION
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()

# CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES - BALANCE & ACCOUNT NO. , CREATE ,METHODS FOR DEBIT, CREDIT,& PRINTING THE BALANCE.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 952551)
acc1.debit(1000)
acc1.credit(500)

