class Student():
    def __init__(self, name="noName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
    print("Hi,nihao a ")


print("我是模块P01")