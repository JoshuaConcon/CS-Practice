#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    b_actual = 0
    for i in range(n):
        if i != k:
            b_actual += ar[i]/2
    if b == b_actual:
        res = "Bon Appetit"
    else:
        res = int(b - b_actual)
    return res

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
