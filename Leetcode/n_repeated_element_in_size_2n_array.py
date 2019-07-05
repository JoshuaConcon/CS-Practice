class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        elements_traversed = set()
        for element in A:
            if(element not in elements_traversed):
                elements_traversed.add(element)
            else:
                return element
