# -*- coding: utf-8 -*-

n = int(input())
for i in range(1,n+1):
    a = " "*(n-i)
    b = "*"*(2*i-1)
    print(a+b)
for j in range(1,n):
    a = " "*j
    b = "*"*(2*(n-j)-1)
    print(a+b)
