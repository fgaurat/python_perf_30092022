import traceback

class DivBy12Error(Exception):

    def __init__(self):
        super().__init__("Division par 12")

def div(a,b):
    if b == 12:
        raise DivBy12Error()

    return a/b


def call_div(a,b):
    r = 0
    try:
        print("ouverture du fichier")
        r = div(a,b)
    finally:    
        print("fermeture du fichier")

    return r

def main():
    try:
        
        b = int(input("b : "))
        a=1
        c = call_div(a,b)
        print(c)


    except ZeroDivisionError as e:
        print('erreur ! ',e)
        traceback.print_exc()
    except TypeError as e:
        print('erreur ! ',e)
        traceback.print_exc()
    except ValueError as e:
        print('erreur ! ',e)
        traceback.print_exc()
    except Exception as e:
        print('erreur ! ',e)
        traceback.print_exc()
    else:
        print("pas d'erreur")

    print("La suite ...")
if __name__ == '__main__':
    main()