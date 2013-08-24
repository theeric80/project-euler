from itertools import product, combinations
from emath import profile

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

# Large non-Mersenne prime
def problem97():
    n = 28433 * 2**7830457 + 1
    ret = int(str(n)[-10:])

    assert(ret == 8739992577)
    print 'problem97 = %d' % ret

if __name__ == '__main__':
    for i in xrange(90, 100):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
