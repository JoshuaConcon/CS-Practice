import operator
import functools

def main(array):
    """
    Given an array of integers, return a new array such that each element at index
    i of the new array is the product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be
    [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    # Best solution: O(n)

    # Get the muliplied result of all items in the list
    product = functools.reduce(operator.mul, array, 1)

    # get the array and divide the product by each index in that array
    result = list(map((lambda x: product / x if x!=0 else product), array))

    return result

print(main([1, 2, 3, 4, 5]))
