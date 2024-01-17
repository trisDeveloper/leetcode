# 108. Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        node = len(nums) // 2
        if not len(nums):
            return None
        return TreeNode(
            nums[node], 
            self.sortedArrayToBST(nums[:node]), self.sortedArrayToBST(nums[node + 1 :])
        )

   
