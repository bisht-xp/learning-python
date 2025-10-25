# Inorder

class Node:
    def __init__(self, d: int):
        self.data = d
        self.left = None
        self.right = None
    

def buildTree():
    d = int(input())

    if(d == -1):
        return None
    
    root = Node(d)
    root.left = buildTree()
    root.right = buildTree()
    return root

def printInorder(node: Node):
    if(node == None):
        return
    
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)


n = buildTree()
printInorder(n)
