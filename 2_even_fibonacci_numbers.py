#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num1 = 1
    num2 = 1
    sum = 0
    x = 0
    
    while x <= n:
        x = num1 + num2
        num1 = num2
        num2 = x
        if x > n:
            break
        if x % 2 == 0:
            sum += x
    print(sum)
