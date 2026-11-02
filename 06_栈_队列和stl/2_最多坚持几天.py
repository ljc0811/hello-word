# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = int(data[1])
    c = [int(x) for x in data[2 : 2 + a]]
    d = [int(x) for x in data[2 + a : 2 + 2 * a]]   
    e = sum(d)
    f = []  
    for i in range(a):
        f.append(c[i] - d[i])      
    f.sort(reverse=True)  
    g = e + sum(f[:b])  
    print(g)
