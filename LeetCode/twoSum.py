# second attempt: a lot faster and efficient
# uses less overhead, is the solution I found on leetcode
# the lesson here is to try to not do anything too fancy
def twoSum2(nums,target):
    seen = dict()
    for indexA, numA in enumerate(nums):
        numB = target - numA
        if numB in seen:
            indexB = seen[numB]
            return [indexB, indexA]
        else:
            seen[numA] = indexA

# first attempt: too slow and inefficient
# too much list comprehension
def twoSum(nums, target):
    '''
    we're looking for numbers that sum up to target
    so we can assume that nums[a] + nums[b] = target
    and that target - nums[b] = nums[a], so we'll store
    the difference of the target and each element in a
    dict and find the match that way
    '''

    # get tuples of indexes i to target - nums[i]
    arrayOfDiffs = [ target-num for num in nums ]
    indexesToDiffTuples = enumerate(arrayOfDiffs)
    # swap elements in tuples
    swapPair = lambda pair : (pair[1], pair[0])
    diffToIndexesTuples = [swapPair(pair) for pair in indexesToDiffTuples]
    # build dict from tuples
    diffToIndexes = dict(diffToIndexesTuples)
    # search dict for collisions
    # if found, return both indexes
    firstIndex = lambda num : nums.index(num)
    secondIndex = lambda num : diffToIndexes[num]
    # this is under the assumption that all elements
    # are unique, so this check that the first and second
    # indexes are different is required
    numIsADiff = lambda num : num in diffToIndexes and (firstIndex(num) != secondIndex(num))
    results = lambda num : [firstIndex(num), secondIndex(num)]
    returnPairList = [ results(num) for num in nums if numIsADiff(num) ]
    return returnPairList[0]
