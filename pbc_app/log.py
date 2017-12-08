def arguments_log(func):
    def wrapper(*args):
        str_args = ','.join(map(lambda i: str(i), args))
        print '{}({})'.format(func.func_name, str_args)
        return func(*args)

    return wrapper
