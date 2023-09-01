from collections import *


def f(n):
    if n == 0:
        return 0
    q = deque([(n, 0)])
    seen = set()
    while q:
        a, d = q.popleft()
        if a == 0:
            return d
        for x in q:
            for nx in (a - x, a + x):
                if nx not in seen and abs(nx - n) < 10 * 10 * 10 * 10 * 10:
                    seen.add(nx)
                    q.append((nx, d + 1))
