def getAllConsecutivePairs(arr):
    return [[i,j] for i,j in zip(arr, arr[1:])]

def getMinAbsDiff(pairs):
    return min([ abs(pair[0]-pair[1]) for pair in pairs])

def getMinAbsDiffPairs(pairs):
    minAbsDiff = getMinAbsDiff(pairs)
    return [pair for pair in pairs if abs(pair[0]-pair[1]) == minAbsDiff]

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sortedArr = sorted(arr)
        consecutivePairs = getAllConsecutivePairs(sortedArr)
        return getMinAbsDiffPairs(consecutivePairs)
