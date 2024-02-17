from Classes.ordinary_client import OrdinaryClient
from Interfaces.i_actor_behaviour import iActorBehaviour


class TaxInspector(iActorBehaviour):
    def __init__(self):
        self.name = "Tax audit"
        self.isTakeOrder = False
        self.isMakeOrder = False


    def getName(self):
        return self.name

    def isTakeOrder(self):
        return self.isTakeOrder

    def isMakeOrder(self):
        return self.isMakeOrder

    def setTakeOrder(self, take):
        self.isTakeOrder = take

    def setMakeOrder(self, make):
        self.isMakeOrder = make

    def getActor(self):
        return OrdinaryClient(self.name).getName()