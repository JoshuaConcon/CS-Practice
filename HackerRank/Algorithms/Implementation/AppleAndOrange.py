#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

a_count = 0
o_count = 0

for apl in apple:
    if apl > 0:
        apl_loc = a+apl
        if ((apl_loc >= s) and (apl_loc <= t)):
            a_count += 1

for orng in orange:
    if orng < 0:
        orng_loc = b+orng
        if ((orng_loc >= s) and (orng_loc <= t)):
            o_count += 1

print(a_count)
print(o_count)
