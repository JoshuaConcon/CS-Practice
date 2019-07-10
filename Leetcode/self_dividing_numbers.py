def get_numbers_inside(num: int) -> List[int]:
    return list(filter(lambda x: x != 0, [int(str_num) for str_num in list(str(num))]))

def check_if_inside(inside_num: int, num: int) -> bool:
    return (num % inside_num == 0)

def is_self_dividing(num: int) -> bool:
    return all([check_if_inside(inside_num, num) for inside_num in get_numbers_inside(num)])

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num_range = [num for num in range(left,right+1) if '0' not in str(num) ]
        return list(filter(is_self_dividing, num_range))
