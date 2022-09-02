def fib(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b



def mult2(a):
    for value in a:
        yield value*2


def get_even(v):
    for value in v:
        if value %2 ==0:
            yield value

def main():
    # f = fib(500000)
    # l = mult2(f)
    # values = list(l)
    # l = mult2(fib(500000))

    # fib(500000) | get_even | 
    l = get_even(fib(500000))
    
    for value in l:
        print(value)


if __name__ == '__main__':
    main()