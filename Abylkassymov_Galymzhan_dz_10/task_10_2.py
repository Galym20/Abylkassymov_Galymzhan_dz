from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


coat = Coat(50)
suit = Suit(165)
print(coat.calculate)
print(suit.calculate)