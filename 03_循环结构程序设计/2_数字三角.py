# -*- coding: utf-8 -*-

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        a = (i - 1)*i//2+j+1
        print(f"{a:4d}", end="")
    print()
