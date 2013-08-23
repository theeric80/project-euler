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

if __name__ == '__main__':
    for i in xrange(90, 100):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
