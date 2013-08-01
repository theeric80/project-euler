from itertools import count, dropwhile
from emath import prime_sieve, is_permuted

# Consecutive prime sum
def problem50():
    x = 1000000
    ret = []
    primes = prime_sieve(x)
    pool = set(primes)
    for i, p in enumerate(primes):
        n = p
        for j in xrange(i+1, len(primes)):
            n += primes[j]
            if n >= x:
                break
            elif n in pool:
                #print '%6d: %s' % (n, str(primes[i:j+1]))
                ret.append((n, primes[i:j+1]))

    ret = max(ret, key=lambda x: len(x[1]))[0]
    assert(ret == 997651)
    print 'problem50 = %d' % ret

# Permuted multiples
def problem52():
    def match(a):
        return all(is_permuted(a[0], a[i]) for i in xrange(1, len(a)))

    ret = dropwhile(lambda x: not match(x), ([n*i for i in xrange(1, 7)] for n in count(1))).next()
    ret = ret[0]

    assert(ret == 142857)
    print 'problem52 = %d' % ret

if __name__ == '__main__':
    for i in xrange(50, 60):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
