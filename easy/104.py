# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node, n):
            if not node:
                return n
            else:
                
                return( max(recurse(node.left, n+1),recurse(node.right, n+1)))
        return recurse(root, 0)
