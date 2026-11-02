# -*- coding: utf-8 -*-

a = input().strip()
b = 0
c = True
for i in a:
    if i == 'a':
        b += 1
    elif i == 'b':
        b -= 1
        if b < 0:
            c = False
            break
    else:
        c = False
        break
if c and b == 0:
    print("Good")
else:
    print("Bad")
