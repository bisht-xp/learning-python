# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    maxSum = float("-inf")
    def dfs(root):
        if not root:
            return 0
        
        left_node = dfs(root.left)
        right_node = dfs(root.right)

        sum = root.val + left_node + right_node
        # maxSum = max(maxSum, sum)

        return  max(sum, left_node, right_node)
    
    return dfs(root)