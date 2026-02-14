# Default Constructor

class Student():

    #
    def st1(self):
        print("Student 1")


obj1 = Student()
obj1.st1()


print("------")
# User defined constructor without parameter

class Employee():

    def __init__(self):
        print("User Defined Constructor")

    def employee1(self):
        print("Employee 1")

obj = Employee()
obj.employee1()


print("------------")

# User defined constructor with parameter

class Employee():

    def __init__(self, name, age):
        print("User Defined Constructor")
        self.firstName = name
        self.empAge = age
        print(self.firstName)
        print(self.empAge)

    def employee2(self, name, age):
        print("Employee 2")
        self.firstName = name
        self.empAge = age
        print(self.firstName)
        print(self.empAge)

obj = Employee("Omkar", 27)
obj.employee2("John", 21)

print("----------------------")

class Example:
    # x = 25
    def __init__(self):
        print("No args")
        pass
    def __init__(self, x):
        print(x)

# Only the second __init__ is used
obj = Example(2)






