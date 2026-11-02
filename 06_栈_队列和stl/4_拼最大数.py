# -*- coding: utf-8 -*-

import sys
from functools import cmp_to_key
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = data[1:a+1]   
    b.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))    
    print("".join(b))
