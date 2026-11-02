# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = ["zero", "two", "four", "six", "nine"]
    c = ["0", "2", "4", "6", "9"]
    for i in range(1, a + 1):
        d = data[i]
        e = ""
        j = 0
        while j < len(d):
            if d[j] in c:
                e += d[j]
                j += 1
            else:
                f = False
                for k in range(5):
                    if d.startswith(b[k], j):
                        e += c[k]
                        j += len(b[k])
                        f = True
                        break
                if not f:
                    j += 1
        print(e)
