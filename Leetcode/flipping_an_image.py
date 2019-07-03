def flip_row(row: List[int]) -> List[int]:
    return row[::-1]

def flip_image_horizontally(image: List[List[int]]) -> List[List[int]]:
    return [flip_row(row) for row in image]

def invert_bit(bit: int) -> int:
    return 0 if (bit) else 1

def invert_row(row: List[int]) -> List[int]:
    return [invert_bit(bit) for bit in row]

def invert_image(image: List[List[int]]) -> List[List[int]]:
    return [invert_row(row) for row in image]

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return invert_image(flip_image_horizontally(A))
