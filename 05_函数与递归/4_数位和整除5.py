# -*- coding: utf-8 -*-

a, b = map(int, input().split())
c = 0
for i in range(a, b + 1):
    d = sum(int(j) for j in str(i))
    if d % 5 == 0:
        c += 1
print(c)
