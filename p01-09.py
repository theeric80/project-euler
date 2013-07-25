import itertools
from itertools import ifilter, takewhile
from emath import fibonacci_n, prime_factor, is_prime, is_palindrome, prime_sieve

# Multiples of 3 and 5
def problem1():
    x = 1000
    ret = sum(i for i in xrange(3, x) if i % 3 == 0 or i % 5 == 0)

    assert(ret == 233168)
    print 'problem1 = %d' % ret

# Even Fibonacci numbers
def problem2():
    x = 4 * 1e+6
    # fib sequence whose values do not exceed x
    fib = takewhile(lambda i: i < x, (fibonacci_n(n) for n in itertools.count(1)))
    #ret = sum(ifilter(lambda i: i % 2 == 0, fib))
    ret = sum(i for i in fib if i % 2 == 0)

    assert(ret == 4613732)
    print 'problem2 = %d' % ret

# Largest prime factor
def problem3():
    x = 600851475143
    factors = prime_factor(x)
    ret = max(i for i in factors.keys())

    assert(ret == 6857)
    print 'problem3 = %d' % ret

# Largest palindrome product
def problem4():
    ret = -1
    for u in xrange(999, 99, -1):
        for v in xrange(999, 99, -1):
            n = u * v
            if n <= ret:
                break
            if not is_palindrome(n):
                continue
            ret = n
            break

    assert(ret == 906609)
    print 'problem4 = %d' % ret

# Smallest multiple
def problem5():
    x = 20
    ret = 2520
    """
    # Brute-Force method
    for a in itertools.count(2520):
        assert(a < 232792561)
        if not all(a % b == 0 for b in xrange(1, x+1)):
            continue
        ret = a
        break

    assert(ret == 232792560)
    print 'problem5 = %d' % ret
    """

# Sum square difference
def problem6():
    """
    sum(1 to n)     = n(n+1)/2
    sum(1^2 to n^2) = n(n+1)(2n+1)/6
    """
    x = 100
    a = sum(i**2 for i in xrange(1, x+1))
    b = sum(i for i in xrange(1, x+1)) ** 2
    ret = b - a

    assert(ret == 25164150)
    print 'problem6 = %d' % ret

# 10001st prime
def problem7():
    x = 10001
    n = 1
    # 2 was 1-st prime, i start from 3, step 2
    for i in itertools.count(3, 2):
        if is_prime(i):
            n += 1
        if n >= x:
            ret = i
            break

    assert(ret == 104743)
    print 'problem7 = %d' % ret

# Largest product in a series
def problem8():
    x = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""

    # generator: product of five consecutive digits in x
    ge_product = (reduce(lambda a, b: int(a) * int(b), x[i:i+5]) for i in xrange(len(x)-4))
    ret = max(ge_product)

    assert(ret == 40824)
    print 'problem8 = %d' % ret

# Special Pythagorean triplet
def problem9():
    """
    a < b < c
    a^2 + b^2 = c^2
    a + b + c = 1000
    """
    """Brute Force"""
    ret = 1
    for a in xrange(1, 1000):
        for b in xrange(a+1, 1000):
            c = 1000 - b - a
            if c <= b:
                break
            if c**2 - b**2 - a**2 == 0:
                ret = a * b * c
                break

    assert(ret == 31875000)
    print 'problem9 = %d' % ret

    """
    Euclid's formula for generating Pythagorean triples
    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2
    m > n
    """
    """
    (m^2 - n^2) + (2mn) + (m^2 + n^2) = 1000
    ...
    m(m+n) = 500
    """

if __name__ == '__main__':
    for i in xrange(1, 10):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
