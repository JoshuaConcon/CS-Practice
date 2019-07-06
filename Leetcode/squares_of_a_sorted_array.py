class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        nums_squared = [num**2 for num in A]
        return sorted(nums_squared)
        
