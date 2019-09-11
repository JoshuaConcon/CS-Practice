# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if(t1 == None):
            result = t2
        elif(t2 == None):
            result = t1
        else:
            node_val = t1.val + t2.val
            result = TreeNode(node_val)
            result.left = self.mergeTrees(t1.left, t2.left)
            result.right = self.mergeTrees(t1.right, t2.right)
        return result
