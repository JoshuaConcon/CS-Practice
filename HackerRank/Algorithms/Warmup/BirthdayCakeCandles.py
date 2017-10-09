#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    max_element = max(ar)
    res = 0
    for i in range(n):
        if(ar[i] == max_element):
            res += 1
    return res

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
