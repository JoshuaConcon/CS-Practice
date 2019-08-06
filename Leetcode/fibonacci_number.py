# Approach: Use Dynamic Programming to save N-1 and N-2 numbers in an array
# Then the last number of an array of length N should be F(N)

def DP_fib(N: int) -> int:
    fib_nums = [0,1]
    for _ in range(1,N):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return fib_nums[-1]

class Solution:
    def fib(self, N: int) -> int:
        if(N==0):
            return 0
        elif(N==1):
            return 1
        else:
            return DP_fib(N)
