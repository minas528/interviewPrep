def morganAndString(a, b):
    a += chr(ord('Z')+1)
    b += chr(ord('Z')+1)
    res = []
    for _ in range(len(a) + len(b)-2):
        if a < b:
            res.append(a[0])
            a = a[1:]
        else:
            res.append(b[0])
            b = b[1:]
    return ''.join(res)
