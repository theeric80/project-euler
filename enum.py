import math
from itertools import count, dropwhile

def fibonacci_n(x):
    sqrt5 = 5**0.5
    phi = (1 + sqrt5) / 2   # golden ratio
    return int(phi**x / sqrt5 + 0.5)

def triangle_n(x):
    return x * (x + 1) / 2

def square_n(x):
    return x * x

def pentagonal_n(x):
    return x * (3 * x - 1) / 2

def hexagonal_n(x):
    return x * (2 * x - 1)

def heptagonal_n(x):
    return x * (5 * x - 3) / 2

def octagonal_n(x):
    return x * (3 * x - 2)

def fibonacci(start=1):
    a, b = fibonacci_n(start), fibonacci_n(start + 1)
    for i in count(start):
        yield a
        a, b = b, a+b

def champernowne_const(): 
    #  Champernowne constant: 0.12345678910111213141516... 
    for i in count(1): 
        x = str(i) 
        for d in x: 
            yield d 

def triangle(start=1):
    for i in count(start):
        yield triangle_n(i)

def square(start=1):
    for i in count(start):
        yield square_n(i)

def pentagonal(start=1):
    for i in count(start):
        yield pentagonal_n(i)

def hexagonal(start=1):
    for i in count(start):
        yield hexagonal_n(i)

def heptagonal(start=1):
    for i in count(start):
        yield heptagonal_n(i)

def octagonal(start=1):
    for i in count(start):
        yield octagonal_n(i)

def cf_sqrt(n):
    # http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
    # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#sqrtcf
    def step(m, d, a):
        m = d * a - m
        d = (n - m**2) / d
        a = int((a0 + m) / d)
        return m, d, a

    pool = set()
    repeat = []

    #a0 = int(n**0.5)
    a0 = dropwhile(lambda i: i**2 < n, count(1)).next() - 1
    u = step(0, 1, a0)
    while u not in pool:
        pool.add(u)
        repeat.append(u[2])
        u = step(*u)

    return [a0, repeat]

def cf_e():
    # e = [2;1,2,1,1,4,1,1,6,1,1,8,...]
    # The pattern continues with ... 1, 2n, 1, ... repeated for ever
    yield 2
    for i in count(3):
        yield 1 if i % 3 != 1 else 2 * (i / 3)

if __name__ == '__main__':
    print 'Unittest: %s' % __file__
    #raw_input()
