def f(k):
    a = []
    while k:
        if k & 1:
            a.append("7")
            k = (k-1) // 2
        else:
            a.append("8")
            k = (k-2) // 2
    return "".join(a[::-1])
