class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        max_val = max(A)
        max_val_index = A.index(max_val)
        return max_val_index
