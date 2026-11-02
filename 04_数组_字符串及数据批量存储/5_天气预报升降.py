# -*- coding: utf-8 -*-

import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = [int(x) for x in data[1:]]
    c = b[-1]    
    if a == 1 and c != 0 and c != 15:
        print("-1")
    else:
        if c == 0:
            print("UP")
        elif c == 15:
            print("DOWN")
        else:
            d = b[-1] - b[-2]
            if d > 0:
                print("UP")
            else:
                print("DOWN")
