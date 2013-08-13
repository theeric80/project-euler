import math
from itertools import count, dropwhile
from emath import profile, is_square

# Square root digital expansion
def problem80():
    def sqrt_long_div(n, k=100):
        # Digit-by-digit calculation
        # http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
        while n > 99:
            n /= 100

        c, p = 0, 0
        for dummy in xrange(k):
            f, i = math.modf(n)
            n = f * 100
            c = c * 100 + int(i)

            x = dropwhile(lambda x: x * (20*p + x) <= c, (x for x in count(0))).next() - 1
            y = x * (20*p + x)

            p = p * 10 + x
            c -= y

        return p

    x = 100
    ret = 0
    for n in (n for n in xrange(1, x+1) if not is_square(n)):
        root = sqrt_long_div(n)
        ret += sum(int(x) for x in str(root))

    assert(ret == 40886)
    print 'problem80 = %d' % ret

if __name__ == '__main__':
    for i in xrange(80, 90):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
