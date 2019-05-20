def convert_to_binary_str(x):
    return '{0:b}'.format(x)

def compare_str(x: int ,y: int ) -> int:
    # pad out strings if one is uneven
    diff = len(x) - len(y)
    padding = abs(diff)*'0'
    if(diff < 0):
        x = padding + x
    else:
        y = padding + y
    # count comparisons
    return count_comparisons(x,y)

def count_comparisons(x: int, y: int) -> int:
    # edge case
    if(len(x) == 0):
        return 0
    diffs = 0
    for i in range(len(x)):
        if(x[i] != y[i]):
            diffs += 1
    return diffs

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # convert both x and y to binary strings
        x_bin = convert_to_binary_str(x)
        y_bin = convert_to_binary_str(y)
        
        # compare two strings
        return compare_str(x_bin,y_bin)
