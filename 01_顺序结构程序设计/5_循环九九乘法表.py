# -*- coding: utf-8 -*-

for i in range(1,10):
    line=[]
    for j in range(1,i+1):
        line.append(f"{j}*{i}={i*j:2d}")
    print(" ".join(line))
