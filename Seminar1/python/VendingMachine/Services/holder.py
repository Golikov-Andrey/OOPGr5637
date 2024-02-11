from typing import List
from Domain.places import Places


class Holder:
    places: List[Places] = []
    def __init__(self, xSize, ySize):
        # self.places:  = []
        for x in range(xSize):
            for y in range(ySize):
                self.places.append(Places(x, y))


    def release(self, x, y):
        place = next(place for place in self.places if place.getCol() == x and place.getRow() == y)
        return place.setEmpty(True)

    def getBalance(self):
        return 0