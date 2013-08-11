import math
from itertools import count, islice, dropwhile
from fractions import gcd
from emath import profile, prime_sieve, prime_factor_p, phi, is_permuted

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
    for n in xrange(2, x+1):
        a = n
        seq = set()
        while a not in seq:
            seq.add(a)
            a = sum(f[d] for d in str(a))
        if len(seq) == z:
            ret += 1

    assert(ret == 402)
    print 'problem74 = %d' % ret

if __name__ == '__main__':
    for i in xrange(70, 80):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
