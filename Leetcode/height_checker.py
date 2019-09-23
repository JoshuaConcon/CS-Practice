def checkHeights(height1, height2):
    if height1==height2:
        return 0
    else:
        return 1

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        mergedHeights = zip(sortedHeights, heights)
        listOfOutOfOrderHeights = [checkHeights(heightPair[0], heightPair[1]) for heightPair in mergedHeights]
        OutOfOrderCount = sum(listOfOutOfOrderHeights)
        return OutOfOrderCount
