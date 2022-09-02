def main():

    l = [10,20,30,40]
    i = 0
    to_find = 80
    is_found = True
    while i<len(l):
        if l[i] == to_find:
            break
        i+=1
    else:
        is_found = False
    
    print(is_found)


def main02():
    l = [10,20,30,40]
    to_find = 80

    is_found = True
    for i in l:
        print(i)
        if i == to_find:
            break
    else:
        is_found = False
    
    print(is_found)

def main01():
    l = [10,20,30,40]
    to_find = 20

    is_found = False
    for i in l:
        print(i)
        if i == to_find:
            print("found !")
            is_found = True
    
    print(is_found)


if __name__ == '__main__':
    main()