def broken_button(s):
    arr = []
    flip = False
    for i in s:
        if i == "i":
            flip = not flip
        elif flip:
            arr = arr[::-1]
        else:
            arr.append(i)
    if flip:
        arr = arr[::-1]
    return "".join(arr)
