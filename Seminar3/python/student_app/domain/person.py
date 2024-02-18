class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def __str__(self):
        return "Person [name=" + self.name + ", age=" + str(self.age) + "]"


