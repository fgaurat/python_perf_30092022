from Rectangle import Rectangle

def main():
    r = Rectangle(longueur=2,largeur=25)
    r1 = Rectangle(longueur=2,largeur=25)
    print(hex(id(r)))
    print(hex(id(r1)))
    r.longueur = 1000
    print(r1.longueur)


if __name__ == '__main__':
    main()