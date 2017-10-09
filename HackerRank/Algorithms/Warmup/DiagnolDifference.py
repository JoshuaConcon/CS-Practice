#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

pri_diag = 0
sec_diag = 0

for i in range(n):
    pri_diag += a[i][i]

for j in range(n):
    sec_diag += a[j][n-j-1]

if(pri_diag < sec_diag):
    print(sec_diag - pri_diag)
else:
    print(pri_diag - sec_diag)
