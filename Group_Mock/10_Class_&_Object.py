# Class & Object
# Non-Static method

class demo1:

    def m1(self):
        print("This is a method m1")

    def m2(self):
        print("This is method m2")

obj1=demo1()     # object = className()
obj1.m1()        # object.Method()
obj1.m2()


print("-----")
# Static method
class demo2:
    @staticmethod
    def m1():
        print("this is a method m1")

    @staticmethod
    def m2():
        print("this is a method m2")

demo2.m1()
demo2.m2()


print("-----")
# Static & Non-static
class demo2:

    def m1(self):
        print("this is a method m1")

    @staticmethod
    def m2():
        print("this is a method m2")

obj2=demo2()
obj2.m1()
demo2.m2()

