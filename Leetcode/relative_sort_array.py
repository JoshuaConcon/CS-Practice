# Assuming arr1 has n items and arr2 has k items and that all elements in arr2 are in arr1
# we can assume that getting the elements that arent and are distinct is O(n)
# and sorting with timsort (using sorted) will be O(nlogn)
# so the final complexity is O(nlogn)

# This solution is the most space efficient (14MB in Python3), but not the most time efficient

def get_elems_not_in_distinct(arr1: List[int], arr2: List[int]) -> List[int]:
    return [elem for elem in arr1 if elem not in arr2]

def get_elems_in_distinct(arr1: List[int], arr2: List[int]) -> List[int]:
    return [elem for elem in arr1 if elem in arr2]

def get_index_in_distinct(arr2: List[int]) -> int:
    def a(x: int) -> int:
        return arr2.index(x)
    return a

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        elems_not_in_distinct = get_elems_not_in_distinct(arr1, arr2)
        elems_in_distinct = get_elems_in_distinct(arr1, arr2)
        result = sorted(elems_in_distinct, key=get_index_in_distinct(arr2)) + sorted(elems_not_in_distinct)
        return result
