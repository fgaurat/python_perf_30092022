def make_incrementor(inc):

    def do_inc(value):
        return value+inc
    
    return do_inc

def main():
    inc2 = make_incrementor(inc=2)
    
    r = inc2(value=1) # 3
    print(r)
    r = inc2(value=10) # 12
    print(r)


    f = bigdata([...])

    f(12)
    f(1)
    f(41)

if __name__ == '__main__':
    main()
