def f(n):
    if n == 1:
        return "7"
    elif n == 2:
        return "8"
    p = (n-1)//2
    if n & 1 == 1:
        return f(p) + "7"
    return f(p) + "8"
