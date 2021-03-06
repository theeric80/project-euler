import math
from fractions import gcd
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

def pythagorean_triple(x):
    # Pythagorean triple: a^2 + b^2 = c^2
    # http://en.wikipedia.org/wiki/Pythagorean_triple

    # Euclid's formula: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    # 1) m > n
    # 2) m and n are coprime
    # 3) m - n is odd

    def is_primitive(m, n):
        assert(m > n)
        return gcd(m, n) == 1 and (m - n) % 2 == 1

    sqrt_x = int((x / 2)**0.5)
    for m, n in ((m, n) for m in xrange(2, sqrt_x+1) for n in xrange(1, m) if is_primitive(m, n)):
        a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
        p = a + b + c
        for i, u in enumerate(xrange(p, x+1, p), 1):
            yield i*a, i*b, i*c

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

def convergents(seq):
    # h(0) = a0
    # k(0) = 1
    # h(1) = a(1)a(0) + 1
    # k(1) = a(1)
    # h(n) = a(n)h(n-1) + h(n-2)
    # k(n) = a(n)k(n-1) + k(n-2)
    a0 = seq.next()
    a1 = seq.next()

    h1, k1 = a0, 1
    h2, k2 = a1 * a0 + 1, a1

    yield h1, k1
    yield h2, k2

    for a in seq:
        h, k = a * h2 + h1, a * k2 + k1
        h1, h2 = h2, h
        k1, k2 = k2, k
        yield h, k

if __name__ == '__main__':
    print 'Unittest: %s' % __file__
    #raw_input()
