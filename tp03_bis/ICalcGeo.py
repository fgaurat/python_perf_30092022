from abc import ABCMeta,abstractmethod




class ICalcGeo(metaclass=ABCMeta):

    @abstractmethod
    def surface(self):
        pass

    def hello(self):
        print("Hello")

    # def surface(self):
    #     raise NotImplementedError("Surface !")
