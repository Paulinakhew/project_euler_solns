#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_num = sum([x for x in range(n+1)])
    square_sum = sum_num ** 2
    sum_square = (n * (n + 1) * (2 * n + 1)) // 6
    abs_diff = square_sum - sum_square
    print(abs_diff)
