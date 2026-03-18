from abc import ABC, abstractmethod

class InterfaceSale(ABC):

    @abstractmethod
    def save(self, sale):
        pass

    