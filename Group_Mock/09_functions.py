print("Function without parameter")
print("---")

def f1():
    print("Function f1 started")
    print("Hi")
    print("hello")

def add():
    print("Function add started")
    num1 = 10
    num2 = 50
    print(num1+num2)

f1()
add()


print("---")
print("function with parameters")

def add(num1, num2):
    print(num1+num2)


def mult(num1, num2):
    print(num1*num2)


# add(int(input("Enter the first number: ")), int(input("Enter the second number: ")))
mult(2,10)


print("---")
print("function with return type")

def name():
    firstName = "Omkar"
    return firstName

ob1=name()         # Variable = functionName()
print(ob1)




print("----")
print("Keyword parameter")

def f1(name, address):
    print("Name is",name, "Address is", address)

f1(name = "Omkar", address ="ABC")
f1(address = "XYZ", name = "ABC")


print("----")
print("Function with multiple return type")

def f1(num1,num2, num3,num4):
    add = num1 + num2
    mult = num3 * num4
    return add, mult

result1 = f1(10, 20,2,10)
print(result1)
# print(num6)

