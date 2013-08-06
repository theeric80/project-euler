from itertools import combinations, dropwhile
from collections import deque
from emath import profile, prime_sieve, is_prime_mr

# Prime pair sets
def problem60():
    def match(a, b):
        a, b = str(a), str(b)
        return a != b and is_prime_mr(int(a+b)) and is_prime_mr(int(b+a))

    def intersection(a, b):
        u = set(b)
        return [i for i in a if i in u]

    x = 5
    p = 10000
    primes = prime_sieve(p)
    [primes.remove(n) for n in [2, 5]]

    # Brute Force
    #ret = dropwhile(lambda u: not all(match(a, b) for a, b in combinations(u, 2)), (u for u in combinations(primes, x))).next()

    pool = dict( [a, [b for b in primes if match(a, b)]] for a in primes )

    ret = []
    for a in pool:
        q = deque( [([a], pool[a]),] )
        while len(q) > 0:
            a, b = q.popleft()
            for n in b:
                if n < a[-1]:
                    continue
                i = intersection(b, pool[n])
                if len(i) > 0:
                    q.append((a+[n], i))
                else:
                    ret.append(a+[n])

    ret = min((u for u in ret if len(u) >= x), key=lambda u: sum(u))
    ret = sum(ret)

    assert(ret == 26033)
    print 'problem60 = %d' % ret

if __name__ == '__main__':
    for i in xrange(60, 70):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
