from interface import *
from dish import *

class Order(IClientOrder, IKitchenOrder):
    def __init__(self, dishes, number, listeners):
        self._dishes = dishes
        self.number = number
        self.listeners = listeners

    def GetSimpleMeals(self):
        arr_s_dishes = []
        for dish in self._dishes:
            if isinstance(dish, Combo_dish):
                for s_dish in dish._s_dishes:
                    if not s_dish._isReady:
                        arr_s_dishes.append(s_dish)
            else:
                if not dish._isReady:
                    arr_s_dishes.append(dish)
        return arr_s_dishes

    def AddMeal(self, dish):
        self._dishes.append(dish)

    def GetReceiptInfo(self):
        return [f'{dish._name} - {dish._cost}' for dish in self._dishes]

    def OnOrderReady(self):
        for listener in self.listeners:
            listener.notify(self)

    def MakeMealReady(self, dish):
        arr = self.GetSimpleMeals()
        for k in arr:
            if k == dish:
                k._isReady = True
        arr = self.GetSimpleMeals()
        if len(arr) == 0:
            self.OnOrderReady()
            












