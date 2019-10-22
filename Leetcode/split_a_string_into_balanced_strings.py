class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        # L = -1
        # R = +1
        stack = 0
        for i in range(len(s)):
            if((stack == 1 and s[i] == 'L') or (stack == -1 and s[i] == 'R')):
                res += 1
            if(s[i] == 'R'):
                stack += 1
            elif(s[i] == 'L'):
                stack -= 1
        return res
                
                
