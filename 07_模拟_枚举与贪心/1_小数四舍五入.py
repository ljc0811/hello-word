# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = int(data[1])
    c = list(data[2])
    while b > 0:
        if '.' not in c:
            break
        d = c.index('.')
        e = -1
        for i in range(d + 1, len(c)):
            if c[i] >= '5':
                e = i
                break
        if e == -1:
            break
        b -= 1
        c = c[:e]
        j = e - 1
        while j >= 0:
            if c[j] == '.':
                j -= 1
                continue
            if c[j] == '9':
                c[j] = '0'
                j -= 1
            else:
                c[j] = str(int(c[j]) + 1)
                break
        if j < 0:
            c.insert(0, '1')
    f = "".join(c)
    if '.' in f:
        f = f.rstrip('0').rstrip('.')
    print(f)
