import Rectangle

def main():


    r = Rectangle.Rectangle(longueur=10,largeur=12)
    r1 = Rectangle.Rectangle(longueur=10,largeur=12)
    print("Rectangle r",r)
    print("Rectangle r1",r1)

    print("int(r)",int(r))
    print("str(r)",str(r))
    
    if r == r1:
        print("ok")
    else:
        print("ko")



    # print(r.longueur) # 10
    # print(r.largeur) # 12
    # r.longueur = 20
    # r.largeur = 22
    # print(r.longueur) # 10
    # print(r.largeur) # 12

if __name__ == '__main__':
    main()