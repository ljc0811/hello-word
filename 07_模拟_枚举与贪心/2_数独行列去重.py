# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    cross = {
        '13': '2', '31': '2',
        '46': '5', '64': '5',
        '79': '8', '97': '8',
        '17': '4', '71': '4',
        '28': '5', '82': '5',
        '39': '6', '93': '6',
        '19': '5', '91': '5',
        '37': '5', '73': '5'
    }
    for a in data:
        b = set()
        c = True
        for i in range(len(a)):
            d = a[i]
            if d in b:
                c = False
                break
            if i > 0:
                e = a[i-1] + d
                if e in cross and cross[e] not in b:
                    c = False
                    break
            b.add(d)
        if c:
            print("YES")
        else:
            print("NO")
