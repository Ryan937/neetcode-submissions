# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, prev_max):
            count = 0

            if not node:
                return count

            if prev_max <= node.val:
                count += 1

            return count + dfs(node.left, max(prev_max, node.val)) + dfs(node.right, max(prev_max, node.val))

        return dfs(root, root.val)