#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    sum = 0
    n = int(input().strip())
    n -= 1
    a = n // 3
    b = n // 5
    c = n // 15
    sum = 3 * ( a * (a + 1)) // 2 + 5 * ( b * (b + 1)) // 2 - 15 * ( c * (c + 1)) // 2
    print(sum)