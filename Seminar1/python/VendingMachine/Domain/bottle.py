from Domain.product import Product

class Bottle(Product):
    def __init__(self, price, place, name, id):
        super().__init__(price, place, name, id)
        self.bottleVolume = 0.0

    def __init__(self, price, place, name, id, bottleVolume):
        super().__init__(price, place, name, id)
        self.bottleVolume = bottleVolume

    def getBottleVolume(self):
        return self.bottleVolume

    def setBottleVolume(self, bottleVolume):
        self.bottleVolume = bottleVolume

    def __str__(self):
        return super().__str__() + "\nvolume=" + str(self.bottleVolume)