# -*- coding: utf-8 -*-

a = input()
parts = a.split()
X = int(parts[0])
Y = int(parts[1])
if Y % X == 0:
    Z = X + Y
else:
    Z = Y - X 
print(Z)
