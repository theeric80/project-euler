import math
from os.path import join, split
from itertools import product, combinations
from emath import profile, prime_sieve, prime_factor_p

# Cube digit pairs
def problem90():
    pool = ['%02d' % (i*i) for i in xrange(1, 10)]
    pool = [map(int, list(i)) for i in pool]

    def match(u, v):
        # allow the 6 and 9 to be reversed
        if 6 in u or 9 in u:
            u += (6, 9)
        if 6 in v or 9 in v:
            v += (6, 9)
        return all((c1 in u and c2 in v) or (c1 in v and c2 in u) for c1, c2 in pool)

    CUBE = list(combinations(xrange(0, 10), 6))
    ret = sum(1 for u, v in product(CUBE, CUBE) if match(u, v)) / 2

    assert(ret == 1217)
    print 'problem90 = %d' % ret

# Square digit chains
def problem92():
    x = 10 * 10**6
    D = dict((str(i), i*i) for i in xrange(0, 10))
    C = dict([(1, 1), (89, 89)])
    ret = 0
    # maxn: maximum number by adding the square of the digits in a 7-digits number
    maxn = 9 * 9 * len(str(x - 1))
    for i in xrange(2, x):
        n = i
        while n not in C:
            n = sum(D[c] for c in str(n))
        if i <= maxn:
            C[i] = C[n]
        if C[n] == 89:
            ret += 1
        #print '%2d: %d' % (i, C[i])

    assert(ret == 8581146)
    print 'problem92 = %d' % ret

# Amicable chains
def problem95():
    x = 10**6

    # Divisor function
    # http://en.wikipedia.org/wiki/Divisor_function
    '''
    S = {1:1}
    P = prime_sieve(int(x**0.5))
    def d(p, a):
        return sum(p**i for i in xrange(a+1))

    def sigma(n):
        if n not in S:
            factors = prime_factor_p(n, P)
            S[n] = reduce(lambda a, b: a * b, (d(p, factors[p]) for p in factors)) - n
        return S[n]
    '''

    # Prime Sieve-liked method
    S = [0] * x
    for i in xrange(1, x):
        for n in xrange(2*i, x, i):
            S[n] += i

    def sigma(n):
        return S[n]

    ret = []
    for i in xrange(2, x):
        q = []
        n = i
        while n not in q and n < 1000000:
            q.append(n)
            n = sigma(n)
        if i == n:
            q.append(n)
            ret.append(q)

    ret = min(max(ret, key=len))

    assert(ret == 14316)
    print 'problem95 = %d' % ret

# Large non-Mersenne prime
def problem97():
    n = 28433 * 2**7830457 + 1
    ret = n % 10**10
    # Slow operation because of str with big number n
    #ret = int(str(n)[-10:])

    assert(ret == 8739992577)
    print 'problem97 = %d' % ret

# Largest exponential
def problem99():
    fname = join(split(__file__)[0], 'data', 'p99_base_exp.txt')
    with open(fname) as f:
        x = [map(int, x.split(',')) for x in f.readlines()]

    # http://en.wikipedia.org/wiki/Exponentiation
    # http://en.wikipedia.org/wiki/Logarithm
    # log(x**p, b) = p * log(x, b)
    def _log(u):
        i, (base, exp) = u
        return exp * math.log10(base)

    ret = max(enumerate(x, 1), key=_log)[0]

    assert(ret == 709)
    print 'problem99 = %d' % ret

if __name__ == '__main__':
    for i in xrange(90, 100):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
