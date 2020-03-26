# demo for *args and **kwargs


def add(a, *args, **kwargs):
    c = a
    print('a =', a)
    print('Type of *args:', type(args))
    for i in args:
        c = c + i
    print('Type of *kwargs:', type(kwargs))
    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))
    return c


print(add(2, 0, 0, 0, d=2, e=1))
