import sys
import math
from os.path import join, split
from itertools import count, dropwhile
from emath import profile, is_square
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

if __name__ == '__main__':
    for i in xrange(80, 90):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
