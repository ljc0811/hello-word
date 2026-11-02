# -*- coding: utf-8 -*-

import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
a = input().strip()
b = a + a[-2::-1]
c = int(b)
if is_prime(c):
    print("prime")
else:
    print("noprime")
