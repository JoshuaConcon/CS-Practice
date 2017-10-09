#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

s = 0
for i in range(len(arr)):
    s += arr[i]

maximum = max(arr)
minimum = min(arr)

print(s-maximum, s-minimum)
