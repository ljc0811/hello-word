# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = [int(x) for x in data[1:a+1]]
    b.sort()
    c = True
    for i in range(a - 2):
        if b[i] + b[i+1] > b[i+2]:
            print(b[i], b[i+1], b[i+2])
            c = False
            break       
    if c:
        print("No solution")
