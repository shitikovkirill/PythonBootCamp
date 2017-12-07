def arguments_log(func):
    def wrapper(*args):
        for a in args:
            print 'arg: "{}"'.format(a)
        return func(*args)

    return wrapper
