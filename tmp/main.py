class TestClass(int):
    def __new__(cls, *args, **kwargs):

        return  super(TestClass, cls).__new__(cls, args[0])
    
    def __init__(self):
        print(int(self))

class MonInteger(int):


    def __str__(self):
        print(self)


def main():
    i = TestClass(12)
    print(i)


if __name__ == '__main__':
    main()