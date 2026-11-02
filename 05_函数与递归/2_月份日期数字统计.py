# -*- coding: utf-8 -*-

import sys
for line in sys.stdin:
    data = line.split()
    if not data:
        continue
    a = int(data[0])
    b = int(data[1])
    c = data[2]
    d = "01 03 05 07 08 10 12".split()
    e = "04 06 09 11".split()
    if f"{b:02d}" in d:
        g = 31
    elif f"{b:02d}" in e:
        g = 30
    else:
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            g = 29
        else:
            g = 28           
    h = 0
    for i in range(1, g + 1):
        h += f"{a:04d}-{b:02d}-{i:02d}".count(c)    
    print(h)
