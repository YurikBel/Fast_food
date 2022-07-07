class Dish:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    # @property
    # def name(self):
    #     return self._name
    #
    # @property
    # def cost(self):
    #     return self._cost
    #
    # @cost.setter
    # def cost(self, value):
    #     if value > 0:
    #         self._cost = value

class Combo_dish(Dish):
    def __init__(self, name, cost, _s_dishes):
        super().__init__(name, cost)
        self._s_dishes = _s_dishes


    def check_ready(self):
        if all([dish._isReady for dish in self._s_dishes]):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self._name}'


class Simple_dish(Dish):
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self._isReady = False

    def __repr__(self):
        return f'{self._name}'

    def MarkAsReady(self):
        self._isReady = True
