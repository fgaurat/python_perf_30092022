
import tasks

def main():
    a = tasks.hello.delay()
    
    print(a.get(timeout=3))


if __name__ == '__main__':
    main()