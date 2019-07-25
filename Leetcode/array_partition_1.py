def get_min_of_pair(pair):
    return min(pair[0], pair[1])

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        # even and odd as in even and odd INDEXES of the sorted array
        even_sorted_nums = sorted_nums[::2]
        odd_sorted_nums = sorted_nums[1::2]
        pairs = zip(even_sorted_nums, odd_sorted_nums)
        min_of_pairs = [get_min_of_pair(pair) for pair in pairs]
        return sum(min_of_pairs)
