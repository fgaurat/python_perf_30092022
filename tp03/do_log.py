def do_log(file_name="file.log"):
    def decorator_do_log(func):
        def wrapper(*values):
            print(f'Log before to {file_name}',*values)
            r = func(*values)
            print('Log after',r)
        
        return wrapper
    return decorator_do_log