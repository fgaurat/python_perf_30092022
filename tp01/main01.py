import lemodule as lm
import sys
import copy
# from lemodule import lemodule as lm => c'est mal

def main():
    l = [10,20,30,40,50]
    print(l)
    l[1] = 1000
    print(l)
    l1 = l[1:4]
    print(l1)
    l1 = l[:4]
    print(l1)
    l1 = l[3:]
    print(l1)
    
    print(50*'-')
    l1 = l[:]
    # l1 = l
    l[0]=12
    print(l)
    print(l1)
    print(50*'-')

    m = [
        [0,1],
        [2,3],
        [4,5]
    ]
    # m2 = m[:]
    m2 = copy.deepcopy(m)
    m[0][0] = 1000
    print(m)
    print(m2)



def main02():
    a = 2   # int : inférence de type
    # b = 2
    print(a)
    print(type(a))
    print("getrefcount",sys.getrefcount(2))
    b=2
    print("getrefcount",sys.getrefcount(2))
    print(hex(id(a)))

    # print(b)
    # print(type(b))
    # print(hex(id(b)))

    b=a
    a=3
    print(b)

def hello(s):
    print("main hello "+s)

def main01():
    # lm.hello("Fred")
    lm.hello("Fred")


if __name__ == '__main__':
    main()