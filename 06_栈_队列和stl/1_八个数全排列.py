# -*- coding: utf-8 -*-

import itertools
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in itertools.permutations(a):
    print(" ".join(map(str, i)))
