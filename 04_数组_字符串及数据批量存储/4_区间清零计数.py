# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = int(data[1])
    c = 2   
    d = [1] * (a + 1)    
    for _ in range(b):
        e = int(data[c])
        f = int(data[c + 1])
        c += 2        
        for i in range(e, f + 1):
            d[i] = 0            
    print(sum(d))
