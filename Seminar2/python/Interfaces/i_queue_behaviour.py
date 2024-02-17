from abc import ABC, abstractmethod

class iQueueBehaviour(ABC):
    @abstractmethod
    def takeInQueue(self, actor):
        pass

    @abstractmethod
    def releaseFromQueue(self):
        pass

    @abstractmethod
    def takeOrder(self):
        pass

    @abstractmethod
    def giveOrder(self):
        pass