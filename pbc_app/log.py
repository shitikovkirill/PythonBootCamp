def arguments_log(func):
    def wrapper(*args):
        for a in args:
            print '{}({})'.format(func.func_name, a)
        return func(*args)

    return wrapper
