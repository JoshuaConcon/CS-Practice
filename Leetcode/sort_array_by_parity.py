def get_parity_numbers(numbers: List[int], parity: int) -> List[int]:
    return list(filter(lambda x: x % 2 == parity, numbers))

def get_even_numbers(numbers: List[int]) -> List[int]:
    return get_parity_numbers(numbers, 0)

def get_odd_numbers(numbers: List[int]) -> List[int]:
    return get_parity_numbers(numbers, 1)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_nums = get_even_numbers(A)
        odd_nums = get_odd_numbers(A)
        return even_nums + odd_nums
