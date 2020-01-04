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
    diffToIndexesTuples = [(tup[1], tup[0]) for tup in indexesToDiffTuples]
    # build dict from tuples
    diffToIndexes = dict(diffToIndexesTuples)
    # search dict for collisions
    # if found, return both indexes
    numIsADiff = lambda num : num in diffToIndexes
    results = lambda num : [nums.index(num), diffToIndexes[num]]
    returnPairList = [ results(num) for num in nums if numIsADiff(num) ]
    return returnPairList[0]

print(twoSum([3,2,4], 6))
