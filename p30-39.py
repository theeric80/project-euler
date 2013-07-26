import itertools
from itertools import ifilter, takewhile
from emath import proper_divisor, is_pandigital

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

    ret = sum(ifilter(lambda i: match(i, 5), xrange(2, x+1)))

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
    print 'problem31 = %d' % ret

if __name__ == '__main__':
    for i in xrange(30, 40):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
