def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)


if __name__ == '__main__':
    print(car(cons(4, 2)))
    print(cdr(cons(4, 2)))