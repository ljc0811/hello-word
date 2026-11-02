# -*- coding: utf-8 -*-

data = input().split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = list(range(a))
e = b
while len(d) > 1:
    e = (e + c - 1) % len(d)
    d.pop(e)
print(d[0])
