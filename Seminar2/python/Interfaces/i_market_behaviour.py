from abc import ABC, abstractmethod

class iMarketBehaviour(ABC):
    
    @abstractmethod
    def acceptToMarket(self, actor):
        pass

    @abstractmethod
    def releaseFromMarket(self, actors):
        pass

    @abstractmethod
    def update(self):
        pass