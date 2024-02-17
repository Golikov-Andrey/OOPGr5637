from abc import ABC, abstractmethod

# from Classes.actor import Actor

class iActorBehaviour(ABC):
    @abstractmethod
    def isTakeOrder(self) -> bool:
        pass

    @abstractmethod
    def isMakeOrder(self) -> bool:
        pass

    @abstractmethod
    def setTakeOrder(self, take):
        pass

    @abstractmethod
    def setMakeOrder(self, make):
        pass

    @abstractmethod
    def getActor(self) -> str:
        pass