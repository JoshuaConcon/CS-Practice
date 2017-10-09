#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
neg = 0
zeros = 0

for i in range(n):
    if(arr[i] > 0):
        pos += 1
    elif(arr[i] < 0):
        neg += 1
    else:
        zeros += 1

print(round(pos/n,6))
print(round(neg/n,6))
print(round(zeros/n,6))
