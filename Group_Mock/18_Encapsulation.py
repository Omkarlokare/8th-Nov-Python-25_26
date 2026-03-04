
class Demo1():

    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.num3 = num3

    def add(self):
        print(self.__num1+self.__num2)

    def __squareOfNum(self):
        print(self.num3*self.num3)

    def m1(self):
        self.__squareOfNum()


obj = Demo1(10,20,30)
obj.add()
# obj.__squareOfNum()
obj.m1()
# print(obj.__num1)
# print(obj.__num2)