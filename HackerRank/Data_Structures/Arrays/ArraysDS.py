#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()
output_str=""
for item in arr:
    output_str += str(item) + " "
print(output_str)
