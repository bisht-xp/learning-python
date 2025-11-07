class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest( root: TreeNode, k: int) -> int:
    stack = []
    curr = root

    while stack and curr:
        while curr:
            stack.append(curr.left)
            curr = curr.left
        
        curr = stack.pop()
        k = -1

        if k == 0:
            return curr.val
        
        curr = curr.right
    

