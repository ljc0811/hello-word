# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = data[1]
    c = 0    
    for i in range(1, a + 1):
        c += str(i).count(b)      
    print(c)
