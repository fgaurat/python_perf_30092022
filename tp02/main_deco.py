


def do_log(file_name):
    """
    log inpout and output of do_log function
    """
    def decorator_do_log(func):
        def wrapper(*values):
            print(f'Log before to {file_name}',*values)
            r = func(*values)
            print('Log after',r)
        
        return wrapper
    return decorator_do_log



@do_log("the.log")
def say_hello(name):
    r = f"Hello {name}"
    print(r)
    return r


def main():
    say_hello("Fred")


if __name__ == '__main__':
    main()