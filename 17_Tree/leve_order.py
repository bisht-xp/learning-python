from collections import deque

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

def printLevelOrder(node: Node):
    q = deque()
    q.append(node)
    while(len(q) != 0):
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            ele = q.popleft()
            current_level.append(str(ele.data))

            if(ele.left):
                q.append(ele.left)
            if(ele.right):
                q.append(ele.right)
        
        print("".join(current_level))



n = buildTree()
print("print tree: ")
printLevelOrder(n)