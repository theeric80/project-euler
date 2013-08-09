from itertools import islice, dropwhile
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
    D = {1: set()}
    f37 = 3.0 / 7
    ret = [0, (0, 1)]
    primes = prime_sieve(int(x**0.5) + 1)

    for d in xrange(2, x + 1):
        D[d] = set(prime_factor_p(d, primes).keys())

        # n/d: the first reduced proper fraction for d to the left of 3/7
        # n/d < 3/7 ==> b = int(3.0 / 7 * d)
        b = max(int(f37 * d), 1)
        n = dropwhile(lambda n: D[n].intersection(D[d]), (n for n in xrange(b, 0, -1))).next()

        f = float(n) / d
        if f < f37 and f > ret[0]:
            ret = [f, (n, d)]

    ret = ret[1][0]
    assert(ret == 428570)
    print 'problem71 = %d' % ret

if __name__ == '__main__':
    for i in xrange(70, 80):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
