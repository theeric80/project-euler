import sys
import math
from os.path import join, split
from itertools import count, dropwhile, takewhile, imap
from emath import profile, is_square, prime_sieve
from ealgorithm import Dijkstra

# Square root digital expansion
def problem80():
    def sqrt_long_div(n, k=100):
        # Digit-by-digit calculation
        # http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
        while n > 99:
            n /= 100

        c, p = 0, 0
        for dummy in xrange(k):
            f, i = math.modf(n)
            n = f * 100
            c = c * 100 + int(i)

            x = dropwhile(lambda x: x * (20*p + x) <= c, (x for x in count(0))).next() - 1
            y = x * (20*p + x)

            p = p * 10 + x
            c -= y

        return p

    x = 100
    ret = 0
    for n in (n for n in xrange(1, x+1) if not is_square(n)):
        root = sqrt_long_div(n)
        ret += sum(int(x) for x in str(root))

    assert(ret == 40886)
    print 'problem80 = %d' % ret

# Path sum: two ways
def problem81():
    fname = join(split(__file__)[0], 'data', 'p81_matrix.txt')
    with open(fname) as f:
        P = [map(int, x.split(',')) for x in f.readlines()]

    for m, n in ((m, n) for m in xrange(len(P)) for n in xrange(len(P[0]))):
        if m == 0 and n == 0:
            continue
        L = P[m][n-1] if n - 1 >= 0 else sys.maxint
        U = P[m-1][n] if m - 1 >= 0 else sys.maxint
        P[m][n] += min(L, U)

    ret = P[-1][-1]
    assert(ret == 427337)
    print 'problem81 = %d' % ret

# Path sum: three ways
def problem82():
    # Shortest path problem
    '''
    M = [[131, 673, 234, 103,  18],
         [201,  96, 342, 965, 150],
         [630, 803, 746, 422, 111],
         [537, 699, 497, 121, 956],
         [805, 732, 524,  37, 331]]
    '''
    fname = join(split(__file__)[0], 'data', 'p81_matrix.txt')
    with open(fname) as f:
        M = [map(int, x.split(',')) for x in f.readlines()]

    row, col = len(M), len(M[0])

    def neighbors(u):
        m, n = u
        for v in [(m, n+1), (m-1, n), (m+1, n)]:
            i, j = v
            if i >= 0 and i < row and j >= 0 and j < col:
                yield v

    # Build Graph G (Adjacency list)
    G = dict()
    for u in ((m, n) for m in xrange(row) for n in xrange(col)):
        G[u] = [[(i, j), M[i][j]] for i, j in neighbors(u)]

    # minimum path sum from (m, 0)
    dst = [(m, col-1) for m in xrange(row)]
    path = (M[m][0] + min(Dijkstra(G, (m, 0), dst))[0] for m in xrange(row))

    # minimum path sum for G
    ret = min(i for i in path)

    assert(ret == 260324)
    print 'problem82 = %d' % ret

# Path sum: four ways
def problem83():
    # Build matrix from file
    fname = join(split(__file__)[0], 'data', 'p81_matrix.txt')
    with open(fname) as f:
        M = [map(int, x.split(',')) for x in f.readlines()]
        row, col = len(M), len(M[0])

    # Build Graph G
    def neighbors(u):
        m, n = u
        for i, j in [(m, n-1), (m, n+1), (m-1, n), (m+1, n)]:
            if i >= 0 and i < row and j >= 0 and j < col:
                yield i, j

    G = dict()
    for u in ((m, n) for m in xrange(row) for n in xrange(col)):
        G[u] = [[(i, j), M[i][j]] for i, j in neighbors(u)]

    # Find the minimal path sum from the top left to the bottom right
    src, dst = (0, 0), [(row-1, col-1)]
    ret = M[0][0] + Dijkstra(G, src, dst)[0][0]

    assert(ret == 425185)
    print 'problem83 = %d' % ret

# Counting rectangles
def problem85():
    '''
    # of rectangles in m x n grid:
    sum((m - i + 1) * (n - j + 1) for j in xrange(1, n+1) for i in xrange(1, m+1))
    = (m(m + 1) / 2) * (n(n + 1) / 2)
    '''
    x = 2 * 10**6
    z = sys.maxint
    ret = 1
    for n in xrange(1, 2001):
        for m in xrange(1, 2001):
            i = (m * (m + 1) / 2) * (n * (n + 1) / 2)
            d = abs(x - i)
            if d < z:
                z = d
                ret = m * n
            if i >= x:
                break

    assert(ret == 2772)
    print 'problem85 = %d' % ret

# Prime power triples
def problem87():
    x = 50 * 10**6
    primes = prime_sieve(int(x**0.5)+1)

    def P(exp, n):
        root = int(n**(1.0 / exp))
        return takewhile(lambda p: p <= root, primes)

    ret = set()
    for m in imap(lambda i: i**4, P(4, x)):
        for n in imap(lambda i: i**3, P(3, x - m)):
            for p2 in P(2, x - m - n):
                ret.add(m + n + p2**2)

    ret = len(ret)
    assert(ret == 1097343)
    print 'problem87 = %d' % ret

# Product-sum numbers
def problem88():
    k = 12000
    k2 = k * 2
    def P(d):
        # S = (a1, a2, ... ad)
        # 2 <= a1 <= a2 <= ... <= ad <= x
        x = int(k2 / (2**(d-1)))
        q = [([i], i) for i in xrange(x, 1, -1)]
        while len(q) > 0:
            S, n = q.pop()
            a = S[-1]
            z = len(S)
            if z < d and n * a <= k2:
                q += [(S + [i], n * i) for i in xrange(x, a-1, -1) if n * i <= k2]
            elif z == d:
                yield n, S

    # k <= N <= 2k
    x = dropwhile(lambda x: 2**x <= k2, count(2)).next() - 1
    ret = dict((i, sys.maxint) for i in xrange(2, k+1))

    # n: product-sum number
    # S: set of natural numbers. the product of S = n
    # d: size of set S. d = k - (# of 1 in S)
    for d in xrange(2, x+1):
        for n, S in P(d):
            s = sum(S)
            k = d + (n - s)
            if k in ret and n < ret[k]:
                ret[k] = n

    ret = sum(set(ret[k] for k in ret))
    assert(ret == 7587457)
    print 'problem88 = %d' % ret

if __name__ == '__main__':
    for i in xrange(80, 90):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
