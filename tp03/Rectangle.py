import do_log

class Rectangle:


    def __init__(self,*,longueur,largeur):
        print(f"def __init__(self,*,{longueur=},{largeur=})")
        self._longueur = longueur
        self._largeur = largeur
    

    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur


    def __str__(self):
        # return f"{type(self).__name__}"
        return f"{__class__.__name__} {self._longueur=}, {self._largeur=}"
    
    def __eq__(self,r) -> bool:
        return self._longueur == r._longueur and self._largeur == r._largeur

    def __del__(self):
        print("def __del__(self)")

    def surface(self):
        return self._longueur * self._largeur
    
    def __int__(self):
        return self.surface()