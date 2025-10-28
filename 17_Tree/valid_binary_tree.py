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


def isValidBST(root: TreeNode) -> bool:
    def validate(node, minVal, maxVal):
        if not root:
            return True
        
        if minVal is not None and node.val <= minVal:
            return False
        
        if maxVal is not None and node.val >= maxVal:
            return False
        
        return validate(node.left, minVal, node.val) and validate(node.right, node.val, maxVal)

    return validate(root, None, None)
