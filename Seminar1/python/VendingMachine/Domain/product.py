class Product:
    def __init__(self, price=-1, place=-1, name="Неизвестно", id=-1):
        self.price = price
        self.place = place
        self.name = name
        self.id = id


    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getPlace(self):
        return self.place

    def setPlace(self, place):
        self.place = place

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def __str__(self):
        return "\nPrice = " + str(self.price) + "\n" + "Place = " + str(self.place) + "\n" + "Name = " + self.name + "\n" + "ID = " + str(self.id) + "\n"




