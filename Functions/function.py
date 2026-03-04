# create function

# Function without/zero Parameter
print("--Function without/zero Parameter--")
def f1():
    print("Hello")
    print("Hi")

f1()

print("--Function with Parameter--")

def add(num1, num2):
    print(num1+num2)

add(1,1)


print("Function with single return type")

def greet():
    return "Hello"

ob = greet()
print(ob)

print("Function with multiple return type")

def calc(num1,num2):
    add = num2+num1
    sub = num1-num2
    return add,sub

ob1, ob2 = calc(5,3)
print(ob1)
print(ob2)


