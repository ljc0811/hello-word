# -*- coding: utf-8 -*-

a = list(map(int, input().split()))
b = sum(a)

if b == 0:
    print(-1)
elif b == 1:
    print(next(c for c in range(10) if a[c]))
elif sum(1 for c in range(10) if a[c] % 2) > 1:
    print(-1)
else:
    d = [a[c] // 2 for c in range(10)]
    e = next((str(c) for c in range(10) if a[c] % 2), "")

    f = -1
    for c in range(1, 10):
        if d[c]:
            f = c
            break
    if f == -1:
        print(-1)
    else:
        d[f] -= 1
        g = str(f) + "".join(str(c) * d[c] for c in range(10))
        print(g + e + g[::-1])
