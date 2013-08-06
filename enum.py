import math
from itertools import count

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

if __name__ == '__main__':
    print 'Unittest: %s' % __file__
    #raw_input()
