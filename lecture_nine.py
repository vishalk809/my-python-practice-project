# # DEL KEYWORD IN OOP:
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("vishal kumar")

del s1
# print(s1)

# PRIVATE(LIKE) ATTRIBUTES & METHODS
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account("952551", "vishal@123")

# print(acc1.acc_no)
# print(acc1.___acc_pass)

# INHERITANCE( SINGLE)
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped." )

class ToyotaCar(Car):
    def __init__(self ,name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)

#  MULTI-LEVEL INHERITANCE
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped." )

class ToyotaCar(Car):
    def __init__(self ,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

# MULTIPLE INHERITANCE
class A :
    varA = "welcome to class A"

class B:
    varB = "wlecome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

# SUPER METHOD
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
         print("car started..")
    
    @staticmethod
    def stop():
         print("car stopped." )     

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type) 

car1 = ToyotaCar("prius", "electric")
print(car1.type)

# CLASS METH0D:
class person:
    name = "vishal kumar"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = person()
p1.changeName("rahul kumar")
print(p1.name)
print(person.name)

# PROPERTY
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) /3) + "%" 

stu1 = Student(97, 98, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)


