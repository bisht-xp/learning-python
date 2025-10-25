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

def printPostOrder(node: Node):
    if(node == None):
        return
    
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data)


n = buildTree()
printPostOrder(n)
    
