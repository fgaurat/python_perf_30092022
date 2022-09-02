from Rectangle import Rectangle


class Carre(Rectangle):
    

    def __init__(self,*,cote=0):
        super().__init__(longueur=cote,largeur=cote)
        print(f"{__class__.__name__} def __init__(self,*,{cote=})")
        self._cote = cote
    
    @property
    def cote(self):
        
        return self._cote

    @cote.setter
    def cote(self,cote):

        self.longueur = cote
        self.largeur = cote
        self._cote = cote
