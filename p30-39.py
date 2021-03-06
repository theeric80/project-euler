import math
import operator
import itertools
from itertools import ifilter, takewhile, imap
from fractions import gcd
from collections import deque
from emath import proper_divisor, is_pandigital, is_prime, prime_sieve, is_palindrome_s, mat_mul

# Digit fifth powers
def problem30():
    # find the upper bound x
    x = 0
    for i in itertools.count(1):
        x = i * 9**5
        if x < int('9'*i):
            break

    def match(a, b):
        return a == sum(int(i)**b for i in str(a))

    ret = sum(i for i in xrange(2, x+1) if match(i, 5))
    #ret = sum(ifilter(lambda i: match(i, 5), xrange(2, x+1)))

    assert(ret == 443839)
    print 'problem30 = %d' % ret

# Coin sums
def problem31():
    x = 200
    ret = []

    # init
    pence = [1, 2, 5, 10, 20, 50, 100, 200]
    stack = list([i] for i in takewhile(lambda n: n<=x, pence))

    # tree traverse
    while len(stack) > 0:
        it = stack.pop()
        n = it[-1]

        # Count the remaining money r
        r = x - sum(it)
        if r < 0:
            continue
        elif r == 0:
            #print it
            ret.append(it)
            continue

        for i in takewhile(lambda a: a<=n, pence):
            stack.append( it+[i] )

    ret = len(ret)
    assert(ret == 73682)
    print 'problem31 = %d' % ret

# Pandigital products
def problem32():
    a = 1000
    b = 10000
    ret = set()
    for i in xrange(a, b+1):
        divisors = proper_divisor(i)[1:]    # remove divisor 1
        for d in divisors:
            q = i / d   # i = d * q
            x = str(i) + str(d) + str(q)
            if is_pandigital(int(x), 9):
                ret.add(i)

    ret = sum(ret)
    assert(ret == 45228)
    print 'problem32 = %d' % ret

# Digit canceling fractions
def problem33():
    def match(n, d):
        # Find the common digits
        pool = [i for i in str(n) if i in str(d)]
        for c in pool:
            # Remove common digit from n, d
            a = int( str(n).replace(c, '') )
            b = int( str(d).replace(c, '') )
            # Test
            if float(n) / d == float(a) / b:
                #print '(%d, %d) -> (%d, %d)' % (n, d, a, b)
                return True
        return False

    # trivial examples for n, d
    # 1) 10, 20, ... 2) 11, 22, ...
    trivial = set(range(10, 100, 10) + range(11, 100, 11))

    # n:numerator, d:denominator, n < d
    ret = []
    for n in xrange(10, 100):
        for d in xrange(n+1, 100):
            if n in trivial or d in trivial:
                continue
            if match(n, d):
                ret.append((n, d))

    # n/d product of the matched numerator/denominator
    n, d = reduce(lambda u, v: tuple(imap(operator.mul, u, v)), ret)
    ret = d / gcd(n, d) # Fraction in Lowest Terms, Reduced Form

    assert(ret == 100)
    print 'problem33 = %d' % ret

# Digit factorials
def problem34():
    # find the upper bound x
    x = 0
    for i in itertools.count(1):
        x = i * math.factorial(9)
        if x < int('9'*i):
            break

    def match(a):
        return a == sum(math.factorial(int(i)) for i in str(a))

    ret = sum(i for i in xrange(3, x+1) if match(i))
    #ret = sum(ifilter(lambda i: match(i), xrange(3, x+1)))

    assert(ret == 40730)
    print 'problem34 = %d' % ret

# Circular primes
def problem35():
    x = 1000000

    def rotate(n):
        x = str(n)
        return (int(x[i:] + x[:i]) for i in xrange(len(x)))

    # method 1: Brute Force
    def match1(n):
        return all(imap(is_prime, rotate(n)))

    # method 2: Prime Sieve
    primes = set(prime_sieve(x))
    def match2(n):
        return all(i in primes for i in rotate(n))

    #ret = len([i for i in xrange(3, x+1, 2) if match1(i)]) + 1
    ret = len([i for i in xrange(3, x+1, 2) if match2(i)]) + 1

    assert(ret == 55)
    print 'problem35 = %d' % ret

# Double-base palindromes
def problem36():
    x = 1000000

    def match(a):
        # bin(a): binary representation of a
        return is_palindrome_s(str(a)) and is_palindrome_s(bin(a)[2:])

    # The last bit of bin(n) must be 1, so check Odd numbers only
    ret = sum([i for i in xrange(1, x+1, 2) if match(i)])

    assert(ret == 872187)
    print 'problem36 = %d' % ret

# Truncatable primes 
def problem37():
    def truncatable(a):
        x = str(a)
        l = [int(x[i:]) for i in xrange(0, len(x))]
        r = [int(x[:i]) for i in xrange(len(x), 0, -1)]
        return all(is_prime(n) for n in l+r)

    ret = []
    for i in itertools.count(11, 2):
        if len(ret) >= 11:
            break
        if not truncatable(i):
            continue
        ret.append(i)

    ret = sum(ret)
    assert(ret == 748317)
    print 'problem37 = %d' % ret

# Pandigital multiples
def problem38():
    def match(a):
        x = ''
        for n in itertools.count(1):
            x += str(a * n)
            if len(x) > 9:
                break
            elif len(x) == 9 and is_pandigital(x, 9):
                #print '%d * [1-%d] = %s' % (a, n, x)
                return int(x)
                break
        return 0

    ret = max(match(i) for i in xrange(9876, 0, -1))

    assert(ret == 932718654)
    print 'problem38 = %d' % ret

# Integer right triangles
def problem39():
    '''
    a + b + c = p
    a^2 + b^2 = c^2
    a <= b < c
    '''
    x = 1000

    # Primitive Pythagorean Triples
    # http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
    # http://mathworld.wolfram.com/PythagoreanTriple.html
    A = [[ 1,  2,  2], [-2, -1, -2], [2, 2, 3]]
    B = [[ 1,  2,  2], [ 2,  1,  2], [2, 2, 3]]
    C = [[-1, -2, -2], [ 2,  1,  2], [2, 2, 3]]
    M = [A, B, C]

    # Tree of Primitive Pythagorean Triples
    q = deque([[[3, 4, 5]],])
    pool = dict((i, []) for i in xrange(1, x+1))
    while len(q) > 0:
        i = q.popleft()
        p = sum(i[0])
        #print '%s' % i[0]
        if p <= x:
            pool[p] += i[0]
            q += [mat_mul(i, m) for m in M]

    # If (a, b, c) is a Pythagorean triple, then so is (ka, kb, kc)
    ret = []
    for i in xrange(12, x+1):
        ret.append( (i, [d for d in (proper_divisor(i)+[i]) if pool[d]]) )

    ret = max(ret, key=lambda i: len(i[1]))[0]
    assert(ret == 840)
    print 'problem39 = %d' % ret

    '''
    def match(p):
        ret = []
        for a in xrange(1, p/3+1):
            for b in xrange(a, (p-a)/2+1):
                c = p - a - b
                #assert(b <= c)
                if c**2 == a**2 + b**2:
                    #print '%4d: {%d, %d, %d}' % (p, a, b, c)
                    ret.append((p, a, b, c))
        return (p, len(ret))

    ret = max((match(p) for p in xrange(x, 3, -1)), key=lambda i: i[1])[0]

    assert(ret == 840)
    print 'problem39 = %d' % ret
    '''

if __name__ == '__main__':
    for i in xrange(30, 40):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
