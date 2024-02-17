from Classes.actor import Actor


class SpecialClient(Actor):
    def __init__(self, name: str, id):
        super().__init__(name)
        self.idVIP = id


    def isTakeOrder(self):
        return super().getTakeOrder()

    def setTakeOrder(self, takenOrder):
        super().setTakeOrder(takenOrder)

    def isMakeOrder(self):
        return super().getMakeOrder()

    def setMakeOrder(self, makeOrder):
        super().setMakeOrder(makeOrder)

    def getActor(self):
        return self.getName()

    def getName(self):
        return super().getName()

    def setName(self, name):
        super().name = name

    def getIdVIP(self):
        return self.idVIP

    def setIdVIP(self, idVIP):
        self.idVIP = idVIP