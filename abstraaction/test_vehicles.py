from abc import ABC, abstractmethod

class Vehicles(ABC):
    def __init__(self, n, y):
        self.__n = n
        self.__y = y

    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def run():
        pass

class Car(Vehicles):
    def __init__(self, n, y, m):
        super().__init__(n, y)
        self.__engine = m
    def stop(self):
        print("the cat stopped")
    def run(self):
        print("the car just moved")

car = Car("qwerty", 1256, "ewfuhweiu")
car.run()
car.stop()
