#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    #Fibonacci sequence is the sum of the two previous numbers in the sequence
    #assign values to the first two numbers in the sequence
    num1 = 1
    num2 = 1

    #current sum of the numbers is zero
    sum = 0
    # x is a placeholder that is used to represent the next number in the sequence
    x = 0
    
    while x <= n:
        x = num1 + num2 #assign value of the sum of the two previous numbers to x
        num1 = num2
        num2 = x
        if x > n: #checks whether or not we have exceeded the value of the inputted number
            break
        if x % 2 == 0: #checks whether or not x is divisible by 2
            sum += x
    #print the sum to the console
    print(sum)
