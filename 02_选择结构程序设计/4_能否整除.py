# -*- coding: utf-8 -*-

a = input()
parts = a.split()
m = int(parts[0])
n = int(parts[1])
if m % n ==0:
    print('YES')
else:
    print('NO')
