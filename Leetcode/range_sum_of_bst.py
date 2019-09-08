# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def getSumOfRoot(root, L, R) -> int:
    if (L <= root.val <= R):
        return root.val
    else:
        return 0

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if(root == None):
            return 0
        sumOfRoot = getSumOfRoot(root, L, R)
        sumOfLeft = self.rangeSumBST(root.left, L, R)
        sumOfRight = self.rangeSumBST(root.right, L, R)
        return sumOfRoot + sumOfLeft + sumOfRight
