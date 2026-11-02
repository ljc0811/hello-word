# -*- coding: utf-8 -*-

import sys
for a in sys.stdin:             
    if a.strip() == '':          
        continue

    n = int(a) + 1

    for i in range(1, n + 1):
        b = ' ' * (2 * (n - i))  
        c = '*' * i             
        print(b + c)
    for i in range(n - 1, 0, -1):
        b = ' ' * (2 * (n - i))
        c = '*' * i
        print(b + c)
