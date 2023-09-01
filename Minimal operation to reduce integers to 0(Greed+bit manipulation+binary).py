from functools import cache


@cache
def f(n):
    if n == 0:
        return 0
    ans = 0
    while n > 0:
        if n & 3 == 3:
            n += 1
            ans += 1
        else:
            ans += n & 1
            n >>= 1
    return ans
