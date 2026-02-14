print("Single level Inheritance")

class Father():

    def car(self):
        print("Method car from father class")

    def Money(self):
        print("Method Money from father class")

    def Home(self):
        print("Method Home from father class")

class son(Father):

    def Bike(self):
        print("Method bike from father class")


obj = son()
obj.car()
obj.Money()
obj.Home()
obj.Bike()


print("---------------")
print("Multi level Inheritance")


class whatsapp1():

    def chat(self):
        print("Chat feature")

class whatsapp2(whatsapp1):

    def audioCalling(self):
        print("Audio feature")


class whatsapp3(whatsapp2):

    def videoCalling(self):
        print("Video feature")


obj1 = whatsapp3()
obj1.chat()
obj1.audioCalling()
obj1.videoCalling()