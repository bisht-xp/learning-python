class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree() -> TreeNode:
    d = int(input())
    if(d == -1):
        return None
    
    root = TreeNode(d)
    root.left = buildTree()
    root.right = buildTree()

    return root


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    
    return  1 + max(maxDepth(root.left), maxDepth(root.right))


root = buildTree()

print(maxDepth(root))