from abc import ABC, abstractmethod


class IClientOrder(ABC):
    @abstractmethod
    def AddMeal(self, dish):
        pass

    @abstractmethod
    def GetReceiptInfo(self):
        pass


class IKitchenOrder(ABC):
    @abstractmethod
    def MakeMealReady(self, dish):
        pass

    @abstractmethod
    def GetSimpleMeals(self):
        pass
