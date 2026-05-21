class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        THE PROBLEM: Find the maximum depth (longest path from root to leaf) of a binary tree

        PATTERN: Depth-First Search (DFS) / Recursion

        INSIGHT: The maximum depth of any node is 1 plus the maximum depth of its tallest child. 
        An empty tree has a depth of 0.

        THE PLAN:
        1. Base Case: If the root is None, return 0
        2. Recursively find the max depth of the left subtree
        3. Recursively find the max depth of the right subtree
        4. Return 1 + max(left_depth, right_depth)

        Example: Tree root=3, left=9, right=20(left=15, right=7)
        - maxDepth(9) = 1 + max(0, 0) = 1
        - maxDepth(20) = 1 + max(1, 1) = 2
        - maxDepth(3) = 1 + max(1, 2) = 3
        Result: 3

        TIME: O(n) - Visiting every node exactly once
        SPACE: O(h) - Balance of call stack, where h is height. O(n) worst case, O(log n) best case
        """
        if not root:
            return 0
            
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
