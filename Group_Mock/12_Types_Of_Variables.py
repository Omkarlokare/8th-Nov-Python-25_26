# Global variable
print("Global variable")
num = 10

print("Function")
def f1():
    print(num)

f1()

print("Class")
class c1:

    def m1(self):
        print(num)

obj = c1()
obj.m1()


print("-----")
# Local variable
print("Local variable")


def add():
    num1 = 10
    num2 = 20
    print(num1+num2)

def mult(num2, num3):
    print(num2*num3)

add()
mult(10,20)



print("------")
print("Class Variable")

class demo1():

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        print(self.num1+self.num2)

    def mult(self):
        print(self.num1*self.num2)

obj = demo1(10, 20)
obj.add()
obj.mult()