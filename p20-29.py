import math
import itertools
from emath import proper_divisor, is_prime

# Factorial digit sum
def problem20():
    x = 100
    ret = sum(int(i) for i in str(math.factorial(x)))

    assert(ret == 648)
    print 'problem20 = %d' % ret

# Amicable numbers
def problem21():
    x = 10000
    pool = {}
    ret = []
    for a in xrange(2, x+1):
        if a not in pool:
            pool[a] = sum(proper_divisor(a))
        b = pool[a]

        # Ignore a if 1) a was prime 2) a == b
        if b == 1 or a == b:
            continue

        if b not in pool:
            pool[b] = sum(proper_divisor(b))
        c = pool[b]

        # Amicable Numbers
        if a == c:
            ret.append(a)

    ret = sum(ret)
    assert(ret == 31626)
    print 'problem21 = %d' % ret

# Non-abundant sums
def problem23():
    def is_abundant(x):
        return sum(proper_divisor(i)) > i

    x = 28123
    ret = range(1, 12)  # 12 was the smallest abundant number
    pool = set()
    for i in xrange(12, x+1):
        if is_abundant(i):
            pool.add(i)

        if all( (i-a not in pool) for a in pool ):
            ret.append(i)

    ret = sum(ret)
    assert(ret == 4179871)
    print 'problem23 = %d' % ret

# Lexicographic permutations
def problem24():
    x = 1000000
    for i, n in enumerate( itertools.permutations( xrange(10) ) ):
        if i >= x:
            ret = int( reduce(lambda a, b: str(a)+str(b), n) )
            break

    assert(ret == 2783915604)
    print 'problem24 = %d' % ret

# 1000-digit Fibonacci number
def problem25():
    i = 1000
    x = int( '1' + '0' * (i-1) )

    a, b, n = 1, 1, 1
    while a <= x:
        a, b, n = b, a+b, n+1

    ret = n
    assert(ret == 4782)
    print 'problem25 = %d' % ret

# Reciprocal cycles
def problem26():
    x = 1000
    ret = 0

    # Long Division
    # Dividend = Divisor * Quotient + Remainder
    # d = i * q + r
    for i in xrange(2, x+1):
        n = 0
        r = 1
        dividend = {}
        quotient = []
        for idx in itertools.count(0):
            if r == 0:
                break
            elif r in dividend:
                n = idx - dividend[r]
                break
            dividend[r] = idx
            r *= 10
            q = r / i
            r = r % i
            quotient.append(q)

        if n > ret:
            ret = i

    assert(ret == 983)
    print 'problem26 = %d' % ret

# Quadratic primes
def problem27():
    def f(a, b):
        for n in itertools.count(0):
            # Euler quadratic formula
            r = n*n + a*n + b
            if not is_prime(r):
                return n

    n = 0
    ret = 0
    for a in xrange(-1000, 1001):
        for b in xrange(-1000, 1001):
            i = f(a, b)
            if i > n:
                n = i
                ret = a * b
    #max( ((a, b, f(a, b)) for a in xrange(-1000, 1001) for b in xrange(-1000, 1001)), key=lambda u: u[2] )

    assert(ret == -59231)
    print 'problem27 = %d' % ret

# Number spiral diagonals
def problem28():
    x = 1001
    ret = 1
    for i in xrange(3, x+1, 2):
        b = (i-2)*(i-2) + 1 # start element i-th spiral
        z = i * 4 - 4       # # of elements of i-th spiral
        # diagonal elements: b+z/4-1, b+2z/4-1, b+3z/4-1, b+4z/4-1
        ret += sum( b + u*z/4 - 1 for u in xrange(1, 5) )

    assert(ret == 669171001)
    print 'problem28 = %d' % ret

# Distinct powers
def problem29():
    ret = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            ret.add(a**b) 

    ret = len(ret)
    assert(ret == 9183)
    print 'problem29 = %d' % ret

if __name__ == '__main__':
    for i in xrange(20, 30):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
