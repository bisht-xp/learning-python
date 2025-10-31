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

def kthSmallest(root: TreeNode, k: int) -> int:
    def inorder(root, count):
        if not root:
            return None
        
        node_left = inorder(root.left, count)
        if(node_left is not None):
            return node_left
        
        count[0] += 1 
        if(count == k):
            return root.val
        

        return inorder(root.right, count)
    
    return inorder(root, [0])
        