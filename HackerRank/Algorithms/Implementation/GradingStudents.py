#!/bin/python3

import sys

def solve(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            value = grades[i]
            multiple = value//5
            mult_of_five = multiple*5

            if mult_of_five < value:
                mult_of_five += 5

            if ((mult_of_five - value) < 3):
                grades[i] = mult_of_five

    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
