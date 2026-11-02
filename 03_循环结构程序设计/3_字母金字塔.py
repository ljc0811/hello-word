# -*- coding: utf-8 -*-

x = input().strip()
y = ord(x) - ord('A') + 1
for i in range(1,y+1):
    a = " "*(y - i)
    print(a,end="")
    for j in range(i):
        X = chr(ord('A') + j)
        print(X,end="")
    for u in range(i-2 ,-1,-1):
        X  = chr(ord('A') + u)
        print(X,end="")
    print()
