class parent():

    def house(self):
        print("Parent house 3bhk")

class son1():

    def car(self):
        print("Son1 car Honda")

class son2(parent,son1):

    def bike(self):
        print("Son2 bike Yamaha")

obj = son2()
obj.house()
obj.car()
obj.bike()