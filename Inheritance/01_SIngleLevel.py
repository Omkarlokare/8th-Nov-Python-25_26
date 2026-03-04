from openpyxl.worksheet.ole import ObjectPr


class Parent():

    def House(self):
        print("Parent house 1bhk")


class Child(Parent):

    def Car(self):
        print("Child car Honda")


obj = Child()
obj.House()
obj.Car()
