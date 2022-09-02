from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from ICalcGeo import ICalcGeo


def show_surface(o:ICalcGeo):
    print(o.surface())

def main():
    r = Rectangle(longueur=12,largeur=2)
    c = Carre(cote=12)
    ce = Cercle(rayon=12)
    print(c.surface())
    c.cote =5
    print("carre",c.surface())
    print("cercle",ce.surface())

    show_surface(ce)
    print(type(Rectangle))




def main01():
    r = Rectangle(longueur=12,largeur=2)
    r1 = Rectangle(longueur=12,largeur=2)
    r2 = Rectangle(longueur=12,largeur=2)
    print(r)
    print(Rectangle.get_cpt())
    Rectangle.cpt = 1000
    print(Rectangle.get_cpt())
    print(dir(Rectangle))

    r3 = Rectangle.build_from_str("1,2")
    print(r3)

if __name__ == '__main__':
    main()