s1 = "ABC"
print(len(s1))


l1 = ["ABC", 10, 10.5]
print(len(l1))



print("---------------")
print("Method Overriding with single level inheritance")


class father:

    def car(self):
        print("Car : TATA")

    def money(self):
        print("Money : 1lac")

    def home(self):
        print("Home: 1bhk")


class son(father):

    def car(self):                        # Method Overriding
        print("Car : Kia")

    def home(self):                       # Method Overriding
        print("Home: 2bhk")

obj1 = son()
obj1.money()
obj1.car()
obj1.home()



print("---------------")
print("Method Overriding with multilevel inheritance")


class grandFather:

    def car(self):
        print("Car : TATA")

    def money(self):
        print("Money : 1lac")

class father(grandFather):

    def car(self):                          # Method Overriding
        print("Car : Kia")

    def money(self):                        # Method Overriding
        print("Money : 2lac")


class son(father):

    def car(self):                        # Method Overriding
        print("Car : Hyundai")

    def money(self):                       # Method Overriding
        print("Home: 3lac")

obj2 = son()
obj2.money()
obj2.car()
print("---")
obj3 = father()
obj3.money()
obj3.car()


print("---------------")
print("Method Overriding with Super() method ")

class A():

    def m1(self):
        print("Method m1 from base class")

class B(A):
    def m2(self):
        super().m1()
        print("Method m2 from Sub class")

obj4 = B()
obj4.m2()
#
# obj5 = A()
# obj5.m1()


print("------------------")
print("Variable overriding")

class parent:
    name = "abcd"

class child(parent):
    name = "ABCD"                           # Variable override

obj6 = child()
print(obj6.name)

# obj7 = parent()
# print(obj7.name)


print("---------------------------")
print("Method overloading")

class demo:

    def add(self, a=0,b=0,c=0,d=0):
        print(a+b+c+d)

obj8 = demo()
obj8.add()
obj8.add(2,4)
obj8.add(3,5,10,100)

