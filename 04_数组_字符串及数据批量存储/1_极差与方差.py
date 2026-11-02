# -*- coding: utf-8 -*-

import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return   
    a = int(data[0])
    b = 1    
    for l in range(a):
        c = int(data[b])
        b += 1     
        d = -float('inf')
        e = float('inf')
        f = 0
        g = 0        
        for l in range(c):
            h = int(data[b])
            b += 1            
            if h > d:
                d = h
            if h < e:
                e = h
            f += h
            g += h * h    
        i = d - e
        j = f / c
        k = (g / c) - (j * j) 
        print(f"{i} {k:.3f}")
solve()
