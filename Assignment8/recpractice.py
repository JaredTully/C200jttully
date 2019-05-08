def s(n):
    if n == 0:
        return 0
    else:
        return n + s(n-1)

def s1(n):
    return (n * (n+1))/2

def p(n):
    if n == 0:
        return 10000
    else:
        return 0.02 * p(n-1) + p(n-1)

def p1(n):
    return (1.02 ** n) * 10000

def b(n):
    if b == 1:
        return 2
    elif b == 2:
        return 3
    else:
        return b(n-1) + b(n-2)


def c(n):
    if n == 1:
        return 9
    else:
        return 9 * c(n-1) + 10 ** (n-1) - c(n-1)


def d(n):
    if n == 0:
        return 1
    else:
        return 3 * d(n-1) + 1

def d1(n):
    return (3 ** (n + 1) -1)/2
