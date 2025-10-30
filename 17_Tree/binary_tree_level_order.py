from collections import deque

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

def levelOrder( root: TreeNode) -> list[list[int]]:
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        current_level = len(queue)
        collect = []
        node = queue.popleft()
        for _ in range(current_level):
            collect.append(node.val)
            if(node.left):
                queue.append(node.left)
        
            if(node.right):
                queue.append(node.right)

        result.append(collect)
    
    return result
            
