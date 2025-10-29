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

def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if(p.val == root.val or q.val == root.val):
        return root
    elif(p.val < root.val > q.val):
        return lowestCommonAncestor(root.left, p, q)
    elif(p.val > root.val < q.val):
        return lowestCommonAncestor(root.right, p, q)
    
    return root