from ICalcGeo import ICalcGeo
import math

class Cercle(ICalcGeo):
    

    def __init__(self,*,rayon=0):
        print(f"{__class__.__name__} def __init__(self,*,{rayon=})")
        self._rayon = rayon
    
    @property
    def rayon(self):
        
        return self._rayon

    @rayon.setter
    def rayon(self,rayon):

        self._rayon = rayon


    def surface(self):
        return math.pi*self._rayon**2