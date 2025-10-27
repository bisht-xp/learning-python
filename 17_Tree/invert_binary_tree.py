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


def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    templeft = invertTree(root.left)
    tempRight = invertTree(root.right)

    root.left = tempRight
    root.right = templeft

    return root