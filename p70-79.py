from itertools import islice
from emath import profile, prime_sieve, phi, is_permuted

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

if __name__ == '__main__':
    for i in xrange(70, 80):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
