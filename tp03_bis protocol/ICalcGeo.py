from abc import ABCMeta,abstractmethod
from typing import Protocol




class ICalcGeo(Protocol):

    def surface(self):
        pass
