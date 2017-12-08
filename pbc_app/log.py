def arguments_log(func):
    def wrapper(*args):
        for a in args:
            print 'fibonacci_xrange({})'.format(a)
        return func(*args)

    return wrapper
