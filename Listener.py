from abc import ABC, abstractmethod


class Listener(ABC):
    @abstractmethod
    def notify(self, order):
        pass


class Client(Listener):
    def notify(self, order):
        print(f'Можно забирать заказ: {order.number}')


class Kitchen(Listener):
    def notify(self, order):
        print(f'Несите заказ: {order.number} на выдачу')
