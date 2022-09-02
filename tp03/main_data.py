from dataclasses import dataclass

@dataclass
class Rectangle:
    longueur:int=0
    largeur:int=0


    def surface(self):
        return self.longueur * self.largeur



def main():
    r = Rectangle(10,11)
    r1 = Rectangle(10,12)
    print(r,r.surface())
    if r==r1:
        print("ok")
    else:
        print("ko")


if __name__ == '__main__':
    main()