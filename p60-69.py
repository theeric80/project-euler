import enum
from itertools import combinations, count, dropwhile, takewhile
from collections import deque
from emath import profile, prime_sieve, is_prime_mr, is_permuted, is_square
from enum import cf_sqrt, cf_e, convergents

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

# Cyclical figurate numbers
def problem61():
    seq = ['triangle', 'square', 'pentagonal', 'hexagonal', 'heptagonal', 'octagonal']
    pool = []
    def split(n):
        x = str(n)
        return x[:2], x[2:]

    def join(a, b):
        return int(str(a) + str(b))

    def match(a):
        return split(a[0])[0] == split(a[-1])[1]

    class node(object):
        def __init__(self, a, b, c, d):
            self.i      = a
            self.head   = b
            self.tail   = c
            self.cyclic = d

        def next_cyclic_node(self):
            next_seq = [i for i in xrange(0, len(seq)) if i not in self.cyclic[0]]
            for next_i in next_seq:
                if self.tail not in pool[next_i]:
                    continue
                # The last 2 digits of n was the first 2 digits of pool[next_i][next_head]
                next_head = self.tail
                for next_tail in pool[next_i][next_head]:
                    next_cyclic = [ self.cyclic[0] + [next_i], \
                                    self.cyclic[1] + [join(next_head, next_tail)] ]
                    yield node(next_i, next_head, next_tail, next_cyclic)

    # Init 6 sequence numbers
    for f in seq:
        d = {}
        for n in takewhile(lambda n: n < 10000, (n for n in getattr(enum, f)() if n > 999)):
            k, v = split(n)
            d[k] = d.get(k, []) + [v]
        pool.append(d)

    # Tree Traverse
    ret = []
    for h in pool[0]:
        q = deque([node(0, h, t, [[0], [join(h, t)]]) for t in pool[0][h]])
        while len(q) > 0:
            i = q.popleft()
            for n in i.next_cyclic_node():
                if len(n.cyclic[1]) < len(seq):
                    q.append(n)
                elif match(n.cyclic[1]):
                    #print n.cyclic
                    ret.append(n.cyclic[1])

    ret = max(ret, key=lambda u: sum(u))
    ret = sum(ret)

    assert(ret == 28684)
    print 'problem61 = %d' % ret

# Cubic permutations
def problem62():
    x = 5
    ret = []

    pool = {}
    for n in count(345):
        n3 = n**3
        k = ''.join(sorted(str(n3)))
        v = pool.get(k, []) + [n3]
        if len(v) >= x:
            ret = v
            break
        pool[k] = v

    '''
    for n in count(345):
        n3 = n**3
        max_n3 = int(''.join(sorted(str(n3), reverse=True)))
        pool = takewhile(lambda i: i <= max_n3, (i**3 for i in count(n)))
        ret = [i for i in pool if is_permuted(n3, i)]
        if len(ret) >= x:
            #print ret
            break
    '''

    ret = ret[0]
    assert(ret == 127035954683)
    print 'problem62 = %d' % ret

# Powerful digit counts
def problem63():
    def match(i, n):
        return len(str(i)) == n

    ret = 0
    x = dropwhile(lambda i: 10**(i-1) <= 9**i, (i for i in count(1))).next()
    for n in xrange(1, x):
        ret += sum(1 for i in (a**n for a in xrange(1, 10)) if match(i, n))

    assert(ret == 49)
    print 'problem63 = %d' % ret

# Odd period square roots
def problem64():
    def match(n):
        return len(cf_sqrt(n)[1]) % 2 > 0

    x = 10000
    ret = sum(1 for n in xrange(2, x+1) if not is_square(n) and match(n))

    assert(ret == 1322)
    print 'problem64 = %d' % ret

# Convergents of e
def problem65():
    x = 100
    seq = convergents(cf_e())
    e100 = dropwhile(lambda u: u[0] < x, ((i, u) for i, u in enumerate(seq, 1))).next()[1]
    ret = sum(int(x) for x in str(e100[0]))

    assert(ret == 272)
    print 'problem65 = %d' % ret

# Diophantine equation
def problem66():
    # http://en.wikipedia.org/wiki/Diophantine_equation
    # http://en.wikipedia.org/wiki/Pell%27s_equation
    def cf_n(n):
        a0, a = cf_sqrt(n)
        x, z = a0, len(a)
        for i in count(0):
            yield x
            x = a[i % z]

    def match(d, x, y):
        return x**2 - d * y**2 == 1

    x = 1000
    ret = []
    for d in (d for d in xrange(2, x+1) if not is_square(d)):
        seq = convergents(cf_n(d))
        ret += [dropwhile(lambda u: not match(*u), ((d, h, k) for h, k in seq)).next()]

    ret = max(ret, key=lambda x:x[1])[0]

    assert(ret == 661)
    print 'problem66 = %d' % ret

if __name__ == '__main__':
    for i in xrange(60, 70):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
