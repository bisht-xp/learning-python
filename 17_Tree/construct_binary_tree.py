# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def indexElement(self, inorder, element):
        for i  in range(len(inorder)):
            if element == inorder[i]:
                return i

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(self, preorder[1:], inorder[:mid])
        root.right = self.buildTree(self,preorder[mid+1:], inorder[mid+1:])

        return root
    
    