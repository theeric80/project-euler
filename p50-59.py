import math
from itertools import count, dropwhile
from emath import prime_sieve, is_permuted

# Consecutive prime sum
def problem50():
    x = 1000000
    ret = []
    primes = prime_sieve(x)
    pool = set(primes)
    for i, p in enumerate(primes):
        n = p
        for j in xrange(i+1, len(primes)):
            n += primes[j]
            if n >= x:
                break
            elif n in pool:
                #print '%6d: %s' % (n, str(primes[i:j+1]))
                ret.append((n, primes[i:j+1]))

    ret = max(ret, key=lambda x: len(x[1]))[0]
    assert(ret == 997651)
    print 'problem50 = %d' % ret

# Permuted multiples
def problem52():
    def match(a):
        return all(is_permuted(a[0], a[i]) for i in xrange(1, len(a)))

    ret = dropwhile(lambda x: not match(x), ([n*i for i in xrange(1, 7)] for n in count(1))).next()
    ret = ret[0]

    assert(ret == 142857)
    print 'problem52 = %d' % ret

# Combinatoric selections
def problem53():
    a = 1
    b = 100
    x = 1000000

    '''
    Binomial coefficient: http://en.wikipedia.org/wiki/Binomial_coefficient
    Pascal's triangle:  c(n, r) = c(n-1, r-1) + c(n-1, r)
    '''
    # c: Pascal's triangle
    c = [[1] * (b+1) for i in xrange(0, b+1)]
    for n in xrange(2, b+1):
        for r in xrange(1, n):
            # set c(n, r) to x+1 if it is greater than x
            i = c[n-1][r-1] + c[n-1][r]
            c[n][r] = i if i <= x else (x+1)

    ret = sum(1 for n in xrange(2, b+1) for r in xrange(1, n) if c[n][r] > x)

    '''
    # Brute Force
    f = dict((n, math.factorial(n)) for n in xrange(a, b+1))
    f[0] = 1
    def comb(n, r):
        return f[n] / (f[r] * f[n-r])

    ret = sum(1 for n in xrange(a, b+1) for r in xrange(0, n+1) if comb(n, r) > x)
    '''

    assert(ret == 4075)
    print 'problem53 = %d' % ret

if __name__ == '__main__':
    for i in xrange(50, 60):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
