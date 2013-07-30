import itertools
from itertools import permutations
from emath import is_prime

# Champernowne's constant
def problem40():
    def champernowne_const():
        #  Champernowne constant: 0.12345678910111213141516...
        for i in itertools.count(1):
            x = str(i)
            for d in x:
                yield d

    x = [10**i for i in xrange(0, 7)]
    ret = []
    for i, d in enumerate(champernowne_const(), 1):
        if len(x) <= 0:
            break
        if i == x[0]:
            ret.append(int(d))
            x.pop(0)

    ret = reduce(lambda a, b: a * b, ret)

    assert(ret == 210)
    print 'problem40 = %d' % ret

# Pandigital prime
def problem41():
    # 1) SUM(1-9)=45 -> 9-digit pandigital num was diviable by 3.
    # 2) SUM(1-8)=36 -> 8-digit pandigital num was diviable by 3.
    # So start from 7-digit pandigital num
    x = 7
    ret = []
    for n in xrange(x, 0, -1):
        a = ''.join(str(i) for i in xrange(n, 0, -1))
        # p: generator for all n-digit pandigital numbers
        p = (int(''.join(u)) for u in permutations(a))
        ret += [i for i in p if is_prime(i)]

    ret = max(ret)
    assert(ret == 7652413)
    print 'problem41 = %d' % ret

if __name__ == '__main__':
    for i in xrange(40, 50):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
