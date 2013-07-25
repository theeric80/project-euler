import datetime
import itertools
from emath import prime_sieve, proper_divisor, prime_factor

# Summation of primes
def problem10():
    x = 2000000
    ret = sum(prime_sieve(x))

    assert(ret == 142913828922)
    print 'problem10 = %d' % ret

# Highly divisible triangular number
def problem12():
    # triangle number(n) = sum(from 1 ot n) = n(n+1)/2
    x = 500
    ret = 3
    # method 1: find the proper divisors for i-th triangle number
    '''
    for i in itertools.count(2):
        n = i * (i + 1) / 2
        if len(proper_divisor(n)) + 1 >= x:
            ret = n
            break

    assert(ret == 76576500)
    '''

    # method 2: Use integer factorization
    '''
    n = a^m + b^n   # By integer factorization
    # of divisors = (m+1)(n+1)
    '''
    for i in itertools.count(2):
        n = i * (i + 1) / 2
        factors = prime_factor(n)
        if reduce(lambda a, b: a * b, (factors[k] + 1 for k in factors.keys())) >= x:
            ret = n
            break

    assert(ret == 76576500)
    print 'problem12 = %d' % ret

# Longest Collatz sequence
def problem14():
    collatz = {}
    def hailstone(x):
        r = [x]
        n = x
        while n > 1:
            # optimize: cache the collatz sequence
            if collatz.has_key(n):
                r += collatz[n][1:]
                break
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            r.append(n)
        if not collatz.has_key(x):
            collatz[x] = r
        return r

    x = 1000000
    # item = (i, length of i-th collatz chain)
    ret = max( ((i, len(hailstone(i))) for i in xrange(2, x)), key=lambda u: u[1] )[0]

    assert(ret == 837799)
    print 'problem14 = %d' % ret

# Lattice paths
def problem15():
    x = 20
    x += 1  # # of grids to # of points
    # g = [[1] * x] * x # error
    g = [[1] * x for i in xrange(x)]
    for u in xrange(1, x):
        for v in xrange(1, x):
            g[u][v] = g[u-1][v] + g[u][v-1]

    ret = g[-1][-1]
    assert(ret == 137846528820)
    print 'problem15 = %d' % ret

# Power digit sum
def problem16():
    a = 2
    b = 1000
    ret = sum(int(i) for i in str(a**b))

    assert(ret == 1366)
    print 'problem16 = %d' % ret

# Maximum path sum I
def problem18():
    # Binary Tree Maximum Path Sum
    x = \
                                    [[75],
                                   [95, 64],
                                 [17, 47, 82],
                               [18, 35, 87, 10],
                             [20, 04, 82, 47, 65],
                           [19, 01, 23, 75, 03, 34],
                         [88, 02, 77, 73, 07, 63, 67],
                       [99, 65, 04, 28, 06, 16, 70, 92],
                     [41, 41, 26, 56, 83, 40, 80, 70, 33],
                   [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
               [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
           [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
         [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

    # pool: maximum total from n-th node to bottom
    pool = [ x[-1][:] ]
    for l in xrange(len(x) - 2, -1, -1):
        a = list(n + max(pool[-1][i], pool[-1][i+1]) for i, n in enumerate(x[l]))
        pool.append(a)

    ret = pool[-1][0]
    assert(ret == 1074)
    print 'problem18 = %d' % ret

# Counting Sundays
def problem19():
    def is_leap_year(y):
       return (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))

    w = 2   # 1901/1/1 was Tuesday
    cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ret = 0
    for y in xrange(1901, 2001):
        for m in xrange(1, 13):
            if w == 0:
                ret += 1
            d = cal[m]
            if m == 2 and is_leap_year(y):
                d = 29
            w = (w + d) % 7

    assert(ret == 171)
    print 'problem19 = %d' % ret

    # Unittest
    d = datetime.datetime(2001, 1, 1).weekday()
    assert(w == (d + 1) % 7)

if __name__ == '__main__':
    for i in xrange(10, 20):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
