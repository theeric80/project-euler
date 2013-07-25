import itertools
from itertools import ifilter

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

if __name__ == '__main__':
    for i in xrange(30, 40):
        fname = 'problem%d' % i
        func = globals().get(fname)
        if not func:
            print '%s is not exist' % fname
            continue
        func()
