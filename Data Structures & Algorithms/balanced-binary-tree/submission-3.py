# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return 0, True
            
            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)

            height = 1 + max(left_height, right_height)
            balanced = (left_balanced and right_balanced and abs(right_height - left_height) <= 1)

            return height, balanced
    
        height, balanced = check(root)
        return balanced