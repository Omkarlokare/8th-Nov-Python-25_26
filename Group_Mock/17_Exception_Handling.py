print("-----4: Example of Correct way of using Generic exception-------")

a=10
print("Program Started")

try:
    b = int(input("Enter a number: "))
    print(a/b)
except ValueError:
    print("Value Error")
# try:
#     print(a/b)
# except ValueError:
#     print("Value Error")
except ZeroDivisionError:
    print("Zero-Division Error")
except Exception as e:
    print("Generic Exception is Handled")
    print(e)

print("Hi")
print("Hello")
print("Program ended")