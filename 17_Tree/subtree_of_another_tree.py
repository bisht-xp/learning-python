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

def isIdentical(valP, valQ)-> bool:
    return valP == valQ

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if(not p and not q):
        return True
    if(not p or not q):
        return False
    
    if(not isIdentical(p.val, q.val)):
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    
    if not subRoot:
        return True
    
    if not root:
        return False
    
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)        
