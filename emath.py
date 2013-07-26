import math

def is_palindrome(x):
    n = x
    r = 0
    # r = reversed(x)
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return x == r

def is_palindrome_s(x):
    #print '%d ? %s == %s' % (x==x[::-1], x, x[::-1])
    return x == x[::-1]

def is_prime(x):
    # Trial Division
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False

    return all(x % i > 0 for i in xrange(3, int(x**0.5) + 1, 2))

def is_pandigital(i, n):
    x = str(i)
    if len(x) != n:
        return False

    a = ''.join( sorted(set(x)) )
    b = ''.join( str(i) for i in xrange(1, n+1) )
    return a == b

# Remove the duplicated chars from string x
#def remove_dup(x):
#    return ''.join(sorted(set(x), key=x.index))

def prime_sieve(x):
    # Sieve of Eratosthenes
    ret = []
    sieve = [True] * x
    for i in xrange(2, x):
        if not sieve[i]:
            continue
        # i is prime if sieve[i] was True
        ret.append(i)
        for m in xrange(2*i, x, i):
            sieve[m] = False
    return ret

def prime_factor(x):
    ret = {}
    i = 2
    while x > 1:
        if x % i == 0:
            x /= i
            ret[i] = ret.get(i, 0) + 1
        else:
            i += (2 if i > 2 else 1)
    return ret

def proper_divisor(x):
    # divisors <= sqrt(x)
    ret = [1]
    for a in xrange(2, int(x**0.5) + 1):
        if x % a > 0:
            continue
        # a,b was divisors
        b = x / a
        # a == b if x == sqrt(x)**2
        ret += [a, b] if (a != b) else [a]
    return ret

def fibonacci_n(x):
    sqrt5 = 5**0.5
    phi = (1 + sqrt5) / 2   # golden ratio
    return int(phi**x / sqrt5 + 0.5)

def fibonacci_seq(x):
    a, b, n = 1, 1, 1
    while n <= x:
        yield n, a
        a, b, n = b, a+b, n+1

def permutations(iterable):
    # Depth-First-Search: Recursive
    result = []
    def dfs(a, b):
        if len(b) > 1:
            [ dfs(a+[x], b[0:i]+b[i+1:]) for i, x in enumerate(b) ]
        else:
            result.append(a+b)

    dfs([], iterable[:])
    return result

def permutations2(iterable):
    # Depth-First-Search: Non-Recursive
    stack = []      # Use stack to store the tree traverse state
    b = iterable[:]
    b.reverse()

    # init
    [ stack.append( ([x], b[0:i]+b[i+1:]) ) for i, x in enumerate(b) ]

    # tree traverse
    while len(stack) > 0:
        a, b = stack.pop()
        if len(b) > 1:
            [ stack.append( (a+[x], b[0:i]+b[i+1:]) ) for i, x in enumerate(b) ]
        else:
            yield a+b

if __name__ == '__main__':
    print 'Unittest: %s' % __file__
    # TODO: Unittest
    #raw_input()
