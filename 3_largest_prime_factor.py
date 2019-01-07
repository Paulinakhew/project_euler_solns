#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    highest_factor = 1
    while n % 2 == 0:
        highest_factor = 2
        n //= 2
    #at this point the number is odd
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            highest_factor = i 
            n = n // i 
    if n > 2: 
        highest_factor = n 
    
    print(highest_factor)