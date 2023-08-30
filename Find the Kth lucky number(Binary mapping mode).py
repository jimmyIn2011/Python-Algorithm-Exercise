def f(k):
    s = bin(k+1)[3:]
    return s.replace("0", "7").replace("1", "8")
