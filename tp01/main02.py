
# HelloWorld => upper camel case, pascal case
# helloWorld => camel case
# hello_world => snake case
# hello-world => kebab case

from collections import deque

def add(*l):
    r = 0
    for i in l:
        r+=i
    return r

# def hello(**kws):
def hello(name,firstName,age):
    print(name,firstName,age)
    # print("hello",kws['name'],kws['firstName'])

# def hello2(pos1,pos2,/,pos_kw1,pos_kw2,*,kw1,kw2):
# def hello2(*,kw1,kw2):
# def hello2(pos1,pos2,/):


# def hello2(*,name,firstName,age):
def hello2(name,firstName,age,/):
    print(name,firstName,age)

def main():
    l = [10,20,30]
    de = deque(l)

    print(de)
    de.appendleft(0)
    print(de)
    v = de.popleft()
    print(de)
    print(v)

def main04():
    # hello2("GAURAT","Fred","46")
    hello2(name="GAURAT",firstName="Fred",age="46")



def main03():
    d = {"name":"GAURAT","firstName":"Fred","age":46}
    # hello(name="GAURAT",firstName="Fred",age=46)
    hello(**d)


    name,firstName,age = d.values()
    s = "Bonjour {name} {firstName}".format(**d)
    s = f"Bonjour {d['name']} {d['firstName']}"
    
    s = f"Bonjour {name} {firstName:<9} {age}"
    print(s)

def main02():
    l = [10, 20, 30,40]

    # r = add(l) # 60
    
    
    # r = add(10, 20, 30)
    r = add(*l) # 60
    print(r)

    a,b,*c= l
    
    print(a,b,c)



def main01():
    l = [10, 20, 30]

    r=[]
    # Scolaire
    for i in l:
        r.append(i)
    
    print("Scolaire",r)

    # Map
    
    r = list(map(lambda i:i,l))
    print("Map lambda",r)

    r = [i for i in l if i <= 20]
    print("List Comprehensions",r)


if __name__ == '__main__':
    main()