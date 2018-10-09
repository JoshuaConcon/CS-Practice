def main(array, k):
    '''
    (list, float) -> bool

    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?
    '''

    # note that n = length of the array

    # Brute-Force Solution [O(n^2)]

    # Just compare each each element to each other, compare every combination
    # result = False
    # array_length = len(array)
    # for i in range(array_length): # runs O(n) times
    #     element_a = array[i]
    #     for j in range(i+1, array_length): # runs O(n-1) times
    #         element_b = array[j]
    #         if((element_a + element_b) == k): # this comparison cost O(1) time
    #             result = True
    # return result

    # My current best Solution [O(nlogn)], also fulfills the bonus

    result = False

    array_length = len(array)

    # i index starts at the beginning of the array
    i = 0
    # j index starts at the end of the array
    j = array_length - 1

    '''if the array is sorted, then the smaller numbers will be at the front and
    the bigger numbers will be at the end of the array'''
    array.sort()

    # define these outside for only accessing each index once
    a = array[i]
    b = array[j]

    # keep looping until the combination is found or the index's overlap (so it is not found)
    while((not result) and (i < j)):

        sum = a + b

        # if the sum is bigger than k
        if(sum > k):
            # decrement j to decrease b and the sum
            j-=1
            # for only accessing each index once
            b = array[j]
        # if the sum is smaller than k
        elif(sum < k):
            # decrement i to increase a and the sum
            i+=1
            # for only accessing each index once
            a = array[i]
        else:
            result = True

    return result
