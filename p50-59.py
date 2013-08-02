import math
from fractions import Fraction
from itertools import count, dropwhile, combinations
from emath import is_prime, is_prime_mr, prime_sieve, is_permuted, is_palindrome_s

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

# Prime digit replacements
def problem51():
    digits09 = '0123456789'
    digits19 = '123456789'
    def replace(n, m):
        digits = digits19 if 0 in m else digits09
        for r in digits:
            x = list(str(n))
            for i in m:
                x[i] = r
            yield int(''.join(x))

    primes = prime_sieve(1000000)
    pool = set(primes)

    ret = 0
    for i in xrange(primes.index(56003), len(primes)):
        n = primes[i]
        z = len(str(n))
        if ret > 0 and n >= ret:
            break

        # mask: comb(z, 1), comb(z, 2), comb(z, 3), ... comb(z, z-1)
        for mask in (combinations(xrange(z), r) for r in range(1, z)):
            for m in mask:
                # replace: the list of replaced values by mask m
                l = [p for p in replace(n, m) if p in pool]
                if len(l) >= 8:
                    #print '%d: %s : %s' % (n, str(m), str(l))
                    ret = l[0]

    assert(ret == 121313)
    print 'problem51 = %d' % ret

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

# Lychrel numbers
def problem55():
    def rev(n):
        return int(str(n)[::-1])

    def is_lychrel(x):
        n = x
        for i in xrange(50):
            n = n + rev(n)
            if is_palindrome_s(str(n)):
                return False
        return True

    x = 10000
    ret = sum(1 for n in xrange(1, x+1) if is_lychrel(n))

    assert(ret == 249)
    print 'problem55 = %d' % ret

# Powerful digit sum
def problem56():
    def dsum(n):
        return sum(int(x) for x in str(n))

    ret = max(dsum(a**b) for a in xrange(2, 100) for b in xrange(2, 100))

    assert(ret == 972)
    print 'problem56 = %d' % ret

# Square root convergents
def problem57():
    '''
    f(1) = 1 + 1 / 2
    ...
    f(n+1) = 1 + 1 / (2 + (f(n) - 1))
           = 1 + 1 / (1 + f(n))
    '''
    def expand_sqrt2(stop=0):
        f = 1 + Fraction(1, 2)
        for i in count(1):
            if stop and i >= stop:
                break
            yield i, f
            f = 1 + 1 / (1 + f)

    def match(a):
        return len(str(a.numerator)) > len(str(a.denominator))

    x = 1000
    ret = sum(1 for i, f in expand_sqrt2(stop=x+1) if match(f))

    assert(ret == 153)
    print 'problem57 = %d' % ret

# Spiral primes
def problem58():
    def square_spiral(length=0):
        a, n = 1, 1
        for i in count(1, 2):
            if length and i > length:
                break
            yield range(a, a+n)
            a = a + n
            n = (i+2)*(i+2) - i*i

    def diagonal(u):
        z = len(u)
        n = z / 4
        return u[:] if z == 1 else [u[i] for i in xrange(n-1, z, n)]

    a = 0
    for i, u in enumerate(square_spiral(), 1):
        a += sum(1 for n in diagonal(u) if is_prime_mr(n))
        b = i * 4 - 3
        if a > 0 and float(a) / b < 0.1:
            ret = i * 2 - 1
            break

    assert(ret == 26241)
    print 'problem58 = %d' % ret

if __name__ == '__main__':
    for i in xrange(50, 60):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
