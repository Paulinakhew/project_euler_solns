#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    d = 2
    """while n > 1:
        while n % d == 0:
            highest_factor = d
            n = n / d    
        d = d + 1"""
    while n % d == 2:
        n /= 2
    
    print(highest_factor)