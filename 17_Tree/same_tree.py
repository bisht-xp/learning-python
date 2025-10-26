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


p = buildTree()
q = buildTree()

print("is same: ", isSameTree(p, q))