import math
from itertools import count, islice, dropwhile
from fractions import gcd
from emath import profile, prime_sieve, prime_factor_p, phi, is_permuted
from enum import pythagorean_triple

# Totient permutation
def problem70():
    x = 10**7

    # Brute Force
    #ret = [u for u in ((n, phi(n)) for n in xrange(2, x)) if is_permuted(*u)]

    ret = []
    primes = prime_sieve(int(x**0.5) * 2)
    for i, p in enumerate(primes):
        for q in islice(primes, i, None):
            # n is semiprime
            n = p * q
            if n >= x:
                break
            phi_n = (p - 1) * p if p == q else (p - 1) * (q - 1)
            if is_permuted(n, phi_n):
                ret.append((n, phi_n))

    ret = min(ret, key=lambda u: float(u[0])/u[1])[0]

    assert(ret == 8319823)
    print 'problem70 = %d' % ret

# Ordered fractions
def problem71():
    x = 1000000
    f37 = 3.0 / 7
    ret = [0, (0, 1)]
    for d in xrange(2, x + 1):
        # n/d: the first reduced proper fraction for d to the left of 3/7
        # n/d < 3/7 ==> b = int(3.0 / 7 * d)
        b = max(int(f37 * d), 1)
        n = dropwhile(lambda n: gcd(n, d) > 1, (n for n in xrange(b, 0, -1))).next()

        f = float(n) / d
        if f < f37 and f > ret[0]:
            ret = [f, (n, d)]

    ret = ret[1][0]
    assert(ret == 428570)
    print 'problem71 = %d' % ret

# Counting fractions
def problem72():
    x = 1000000
    # n/d is reduced proper fraction if n is relatively prime to d
    # # of reduced proper fraction for d ==> phi(d)
    ret = sum(phi(d) for d in xrange(2, x+1))

    assert(ret == 303963552391)
    print 'problem72 = %d' % ret

# Counting fractions in a range
def problem73():
    x = 12000
    f12 = 1.0 / 2
    f13 = 1.0 / 3

    def match(n, d):
        f = float(n) / d
        return f > f13 and f < f12 and gcd(n, d) == 1

    ret = 0
    for d in xrange(2, x+1):
        a = int(f13 * d) + 1
        b = int(f12 * d)
        ret += sum(1 for n in xrange(a, b+1) if match(n, d))

    assert(ret == 7295372)
    print 'problem73 = %d' % ret

# Digit factorial chains
def problem74():
    x = 10**6
    z = 60
    f = dict((str(n), math.factorial(n)) for n in xrange(0, 10))
    ret = 0
    '''
    for n in xrange(1, x+1):
        a = n
        q = set()
        while a not in q:
            q.add(a)
            a = sum(f[d] for d in str(a))
        if len(q) == z:
            ret += 1
    '''
    D = {1:0, 2:0, 145:0, 169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}
    q = set()

    def chain(n):
        if n in D:
            return D[n]
        elif n in q:
            return 0
        q.add(n)
        a = sum(f[d] for d in str(n))
        return 1 + chain(a)

    for n in xrange(3, x+1):
        D[n] = chain(n)
        q.clear()
        if D[n] == z:
            ret += 1

    assert(ret == 402)
    print 'problem74 = %d' % ret

# Singular integer right triangles
def problem75():
    x = 1500000
    pool = {}
    for a, b, c in pythagorean_triple(x):
        p = a + b + c
        #print '%d: (%d, %d, %d)' % (p, a, b, c)
        pool[p] = pool.get(p, 0) + 1

    ret = sum(1 for p in pool if pool[p] == 1)

    assert(ret == 161667)
    print 'problem75 = %d' % ret

# Counting summations
def problem76():
    # Dynamic Programming
    x = 100 + 1
    M = [[1] * x for i in xrange(x)]
    for m, n in ((m, n) for m in xrange(2, x) for n in xrange(2, x)):
        if m - n >= 0:
            M[m][n] = M[m][n-1] + M[m-n][n]
        else:
            M[m][n] = M[m][n-1]

    ret = M[-1][-1] - 1

    assert(ret == 190569291)
    print 'problem76 = %d' % ret

# Prime summations
def problem77():
    x = 100 + 1
    P = [0] + prime_sieve(x)
    z = len(P)
    M = [[0] * z for i in xrange(x)]

    # Init
    for n in xrange(z):
        M[0][n] = 1

    ret = 0
    for m in xrange(2, x):
        for n in xrange(1, z):
            i = m - P[n]
            if i >= 0:
                M[m][n] = M[m][n-1] + M[i][n]
            else:
                M[m][n] = M[m][n-1]
        #print '%3d: %s' %(m, str(M[m]))
        if M[m][-1] > 5000:
            ret = m
            break

    assert(ret == 71)
    print 'problem77 = %d' % ret

if __name__ == '__main__':
    for i in xrange(70, 80):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
