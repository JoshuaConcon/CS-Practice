class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = ( num for num in A if num % 2 == 0)
        odd = ( num for num in A if num % 2 == 1)
        zippedNums = ( list(pair) for pair in zip(even, odd) )
        return itertools.chain.from_iterable(zippedNums)
