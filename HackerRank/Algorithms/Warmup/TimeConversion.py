#!/bin/python3

import sys

def timeConversion(s):
    s_list = list(s)
    if((s_list[0] == '1') and (s_list[1] == '2')):
        # 12:00
        if(s_list[-2] == 'A'):
            #12:00 AM
            s_list[0] = '0'
            s_list[1] = '0'
    elif(s_list[-2] == 'P'):
        # PM not 12
        s_list[0] = str(int(s_list[0]) + 1)
        s_list[1] = str(int(s_list[1]) + 2)
    return ''.join(s_list[0:-2])

s = input().strip()
result = timeConversion(s)
print(result)
