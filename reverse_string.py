class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        firstIndex = 0
        lastIndex = -1
        for i in range(len(s)//2):
            (s[firstIndex + i], s[lastIndex - i]) = (s[lastIndex - i], s[firstIndex + i])
        
