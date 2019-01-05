#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t): #iterates through each inputted number
    sum = 0
    n = int(input().strip())

    #must exclude n so subtract 1 from n
    n -= 1

    #find the integer representations of n dividided by 3, 5, and 15
    a = n // 3
    b = n // 5
    c = n // 15

    #we find the sum of all the multiples of 3 and 5 using the appropriate formula
    #subtract all the multiples of 15 as they are counted twice
    sum = (3 * ( a * (a + 1)) + 5 * ( b * (b + 1)) - 15 * ( c * (c + 1))) // 2
    
    #print the sum
    print(sum)
