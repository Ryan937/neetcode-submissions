# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = [0]
        self.helper(root, result, float('-inf'))

        return result[0]
    
    def helper(self, root: TreeNode, result: List[int], prevMax: int):
        if not root: return

        if prevMax <= root.val:
            result[0] += 1

        self.helper(root.left, result, max(prevMax, root.val))
        self.helper(root.right, result, max(prevMax, root.val))