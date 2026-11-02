# -*- coding: utf-8 -*-

data = input().split()
a = int(data[0])
b = int(data[1])
c = 0
for i in range(a, b + 1):
    c += str(i).count('2')
print(c)
