#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_dict = dict()
    for i in range(n):
        sock = ar[i]
        if(sock in sock_dict):
            sock_dict[sock] = sock_dict[sock] + 1
        else:
            sock_dict[sock] = 1
    result = 0
    print(sock_dict)
    for key in sock_dict:
        pairs = sock_dict[key]//2
        result = result + pairs
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
