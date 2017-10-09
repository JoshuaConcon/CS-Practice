#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
    a = ''
    for j in range(n):
        if(i >= j):
            a = '#' + a
        else:
            a = ' ' + a
    print(a)
