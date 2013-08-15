import sys
import bisect

def Dijkstra(G, src, dst):
    # Dijkstra's algorithm
    ret = []
    dst = set(dst)
    D = dict([u, sys.maxint] for u in G)
    D[src] = 0
    U = [(D[k], k) for k in D]
    U.sort()
    while len(U) > 0 and len(dst) > 0:
        p, u = U.pop(0)
        for v, dv in G[u]:
            d = p + dv
            if d < D[v]:
                # Update path sum in sorted list U
                i = bisect.bisect_left(U, (D[v], v))
                U = U[:i] + U[i+1:]
                bisect.insort_left(U, (d, v))
                D[v] = d
        if u in dst:
            ret.append((p, u))
            dst.remove(u)
    return ret

if __name__ == '__main__':
    print 'Unittest: %s' % __file__
    # TODO: Unittest
