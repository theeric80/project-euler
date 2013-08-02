import math
from random import randint
import operator
import itertools
from itertools import imap

def profile(func):
    def inner(*args, **kwargs):
        import cProfile
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.print_stats()
        return retval
    return inner

def is_palindrome(x):
    n = x
    r = 0
    # r = reversed(x)
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return x == r

def is_palindrome_s(n):
    x = str(n)
    return x == x[::-1]

def is_square(n):
    root = n**0.5
    return int(root + 0.5)**2 == n

def is_prime(x):
    # Trial Division
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False

    return all(x % i > 0 for i in xrange(3, int(x**0.5) + 1, 2))

def is_prime_mr(n, k=6):
    # Miller Rabin Primality Test
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    # http://rosettacode.org/wiki/Miller-Rabin_primality_test
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False

    # Test a whether it is a witness for the compositeness of n
    def witness(a, n):
        # n - 1 = (2**t)u ; t >= 1, u is odd
        u = n - 1
        t = 0
        while u % 2 == 0:
            u >>= 1
            t += 1

        x = pow(a, u, n)
        if x == 1 or x == n - 1:
            return False

        for i in xrange(t-1):
            x = x**2 % n
            if x == 1:
                return True
            if x == n - 1:
                return False

        return True

    # Miller-Rabin
    return not any( witness(randint(2, n - 1), n) for i in xrange(k) )

def is_pandigital(i, n):
    x = str(i)
    if len(x) != n:
        return False

    #a = ''.join( sorted(set(x)) )
    #b = ''.join( str(i) for i in xrange(1, n+1) )
    #return a == b
    return set(x) == set(str(i) for i in xrange(1, n+1))

def is_permuted(x, y):
    return set(str(x)) == set(str(y))

def is_pentagonal(x):
    return (24 * x + 1)**0.5 % 6 == 5

# Remove the duplicated chars from string x
#def remove_dup(x):
#    return ''.join(sorted(set(x), key=x.index))

def prime_sieve(x):
    # Sieve of Eratosthenes
    ret = []
    sieve = [True] * x
    for i in xrange(2, x):
        if not sieve[i]:
            continue
        # i is prime if sieve[i] was True
        ret.append(i)
        for m in xrange(2*i, x, i):
            sieve[m] = False
    return ret

def prime_sieve_s(x):
    # Segmented Sieve of Eratosthenes
    def mark(sieve, p, start, stop):
        i = max(2, math.ceil(float(start) / p))
        for n in xrange(int(i)*p, stop, p):
            if n not in sieve:
                continue
            sieve[n] = False

    ret = []
    end = bound = 350000
    sieve = dict((n, True) for n in xrange(2, end))
    for i in itertools.count(2):
        if i >= x:
            break
        if i < end and sieve[i]:
            # i was prime
            ret.append(i)
            mark(sieve, i, i, end)
        elif i >= end:
            # assert check
            #b = all((n in ret) == sieve[n] for n in sieve)
            #assert(b)

            # Goto next segment
            end = i + bound
            sieve = dict((n, True) for n in xrange(i, end))
            for p in ret:
                mark(sieve, p, i, end)
    return ret

def prime_factor(x):
    ret = {}
    i = 2
    while x > 1:
        if x % i == 0:
            x /= i
            ret[i] = ret.get(i, 0) + 1
        else:
            i += (2 if i > 2 else 1)
    return ret

def proper_divisor(x):
    # divisors <= sqrt(x)
    ret = [1]
    for a in xrange(2, int(x**0.5) + 1):
        if x % a > 0:
            continue
        # a,b was divisors
        b = x / a
        # a == b if x == sqrt(x)**2
        ret += [a, b] if (a != b) else [a]
    return ret

def fibonacci_n(x):
    sqrt5 = 5**0.5
    phi = (1 + sqrt5) / 2   # golden ratio
    return int(phi**x / sqrt5 + 0.5)

def fibonacci_seq(x):
    a, b, n = 1, 1, 1
    while n <= x:
        yield n, a
        a, b, n = b, a+b, n+1

def triangle_n(x):
    return x * (x + 1) / 2

def pentagonal_n(x):
    return x * (3 * x - 1) / 2

def hexagonal_n(x):
    return x * (2 * x - 1)

def triangle(start=1):
    for i in itertools.count(start):
        yield triangle_n(i)

def pentagonal(start=1):
    for i in itertools.count(start):
        yield pentagonal_n(i)

def hexagonal(start=1):
    for i in itertools.count(start):
        yield hexagonal_n(i)

def permutations(iterable):
    # Depth-First-Search: Recursive
    result = []
    def dfs(a, b):
        if len(b) > 1:
            [ dfs(a+[x], b[0:i]+b[i+1:]) for i, x in enumerate(b) ]
        else:
            result.append(a+b)

    dfs([], iterable[:])
    return result

def permutations2(iterable):
    # Depth-First-Search: Non-Recursive
    stack = []      # Use stack to store the tree traverse state
    b = iterable[:]
    b.reverse()

    # init
    [ stack.append( ([x], b[0:i]+b[i+1:]) ) for i, x in enumerate(b) ]

    # tree traverse
    while len(stack) > 0:
        a, b = stack.pop()
        if len(b) > 1:
            [ stack.append( (a+[x], b[0:i]+b[i+1:]) ) for i, x in enumerate(b) ]
        else:
            yield a+b

def mat_mul(a, b):
    col_b = zip(*b)
    return [[sum(imap(operator.mul, r, c)) for c in col_b] for r in a]

if __name__ == '__main__':
    print 'Unittest: %s' % __file__
    # TODO: Unittest
    #raw_input()
