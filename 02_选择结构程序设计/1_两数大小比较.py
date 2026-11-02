# -*- coding: utf-8 -*-

c = input()
d = c.split()
a = int(d[0])
b = int(d[1])
if a < b:
    print('<')
elif a==b:
    print('=')
else:
    print('>')
